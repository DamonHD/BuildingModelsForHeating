# Docs:
# - https://bigladdersoftware.com/epx/docs/24-2/ems-application-guide/index.html
# - https://bigladdersoftware.com/epx/docs/24-2/ems-application-guide/ems-calling-points.html#ems-calling-points
# - https://bigladdersoftware.com/epx/docs/24-2/input-output-reference/group-python-plugins.html
#
# Examples: `PythonPlugin*` in examples folder


from pyenergyplus.plugin import EnergyPlusPlugin


class BaseboardTotalHeatDemand(EnergyPlusPlugin):
    """Output the total heating demand for radiators in all zones."""

    def __init__(self):
        super().__init__()
        self.rad = None
        self.total_rad_htr = None

    def on_end_of_zone_timestep_before_zone_reporting(self, state) -> int:
        # Cache input and output variable handles
        if self.total_rad_htr is None:
            self.rad = [
                self.api.exchange.get_variable_handle(
                    state, "Baseboard Total Heating Rate", f"Z{i} Radiator"
                )
                for i in range(1, 5)
            ]
            self.total_rad_htr = self.api.exchange.get_global_handle(
                state, "TotalBaseboardHeatTransferRate"
            )

        htr = 0.0
        for handle in self.rad:
            htr += self.api.exchange.get_variable_value(state, handle)

        self.api.exchange.set_global_value(state, self.total_rad_htr, htr)

        return 0


class LoadCompHeatPumpController(EnergyPlusPlugin):
    """Simulates a load compensated control system of a DHW air source heat pump.

    Inputs:
        - Heat pump outlet water temperature (flow temperature)
            - Actual node used is the plant loop supply outlet water temperature
        - Heat pump water inlet temperature (return temperature)
        - Plant loop water mass flow rate
        - Outside air temperature
        - Zone 1 air temperature

    Outputs:
        - Plant loop supply outlet setpoint temperature (flow temperature setpoint)
        - Supply pump mass flow rate setpoint

    Description:
        1) ~~Feed-forward control of flow temperature setpoint based on outside temperature~~
            - This step is ignored as the simulation will converge to the same setpoint
              whether or not it is implemented.
        2) Feed-back control of flow temp setpoint based on Z1 air temp
        3) Feed-back control of water pump flow setpoint based on HP inlet and outlet temperatures
           (attempts to maintain 5 C temp drop)
           - TODO

    Notes:
        - See eplusout.edd for list of actuator variables
    """

    def __init__(self):
        super().__init__()
        self.flow_temp_setpoint = None

        # LC Parameters
        self.flow_setpoint_gain = 0.01
        # FIXME: Hard coded as I couldn't retrieve the value from the simulation for some reason.
        # This should be set to the same value as the Z1 temperature setpoint in the .idf
        self.z1_setpoint_c = 21.0

    def get_flow_temp(self, state) -> int:
        return self.api.exchange.get_actuator_value(state, self.flow_temp_setpoint)

    def set_flow_temp(self, state, t):
        self.api.exchange.set_actuator_value(state, self.flow_temp_setpoint, t)

    def get_val(self, state, handle) -> int:
        return self.api.exchange.get_variable_value(state, handle)

    # This needs to be solved iteratively
    def on_inside_hvac_system_iteration_loop(self, state) -> int:
        if not self.api.exchange.api_data_fully_ready(state):
            return 0

        # TODO: Move this out into another calling point
        if self.flow_temp_setpoint is None:
            print("Using load compensation")

            # Returns a handle to an input variable.
            #
            # NOTE: These are *output* values of the E+ simulation, as written
            # to eplusout.eso and as such, they must be set as 'Output:Variable's
            # in the .idf file.
            def get_var_handle(var, object):
                handle = self.api.exchange.get_variable_handle(state, var, object)
                assert handle != -1, f"Could not get handle to variable {object}:{var}"
                return handle

            # Returns a handle to an actuator variable (i.e. readable and writable).
            #
            # These are generally control outputs for the simulation.
            def get_act_handle(object_type, object, var):
                handle = self.api.exchange.get_actuator_handle(
                    state, object_type, var, object
                )
                assert handle != -1, (
                    f"Could not get handle to actuator {object_type}{object}:{var}"
                )
                return handle

            try:
                # Inputs:
                self.flow_temp = get_var_handle(
                    "Plant Supply Side Outlet Temperature", "HOT WATER LOOP"
                )
                self.return_temp = get_var_handle(
                    "Heat Pump Load Side Inlet Temperature", "Heat Pump"
                )
                self.flow_rate = get_var_handle("Pump Mass Flow Rate", "SUPPLY PUMP")
                self.z1_temp = get_var_handle("Zone Air Temperature", "Z1")
                self.outside_temp = get_var_handle(
                    "Site Outdoor Air Drybulb Temperature", "Environment"
                )
                # Outputs:
                self.flow_temp_setpoint = get_act_handle(
                    "Schedule:Constant", "HP Flow Temp Setpoint", "Schedule Value"
                )
                self.flow_rate_setpoint = get_act_handle(
                    "Pump", "SUPPLY PUMP", "Pump Mass Flow Rate"
                )
                # FIXME: Unused as I couldn't retrieve the value from the simulation.
                # Technically an input but I'm keeping it together with the actuators
                self.z1_setpoint = get_act_handle(
                    "Schedule:Compact", "ALWAYS 21", "Schedule Value"
                )
            except AssertionError as e:
                self.api.runtime.issue_severe(state, str(e))
                return 1

        z1_temp = self.get_val(state, self.z1_temp)
        flow_temp_setpoint = self.get_flow_temp(state)
        flow_temp_setpoint += self.flow_setpoint_gain * (self.z1_setpoint_c - z1_temp)
        self.set_flow_temp(state, flow_temp_setpoint)

        return 0


class WeatherCompHeatPumpController(EnergyPlusPlugin):
    """Simulates a weather compensated control system of a DHW air source heat pump.
    Inputs:
        - Heat pump outlet water temperature (flow temperature)
            - Actual node used is the plant loop supply outlet water temperature
        - Heat pump water inlet temperature (return temperature)
        - Plant loop water mass flow rate
        - Outside air temperature
        - Zone 1 air temperature

    Outputs:
        - Plant loop supply outlet setpoint temperature (flow temperature setpoint)
        - Supply pump mass flow rate setpoint

    Description (Non-HG case):
        1) Feed-forward control of flow temperature setpoint based on outside temperature
           - TODO
        2) Feed-back control of water pump flow setpoint based on flow temperature
           (attempts to maintain steady flow temp)
           - TODO
           - This is automatically handled during normal simulation
        3) Feed-back control of water pump flow setpoint based on HP inlet and outlet temperatures
           (attempts to maintain 5 C temp drop)
           - TODO

    Notes:
        - See eplusout.edd for list of actuator variables
        - Should it control
            1) SUPPLY PUMP OUTLET NODE,System Node Setpoint,Mass Flow Rate Setpoint
            2) SUPPLY PUMP,Pump,Pump Mass Flow Rate
            3) SUPPLY PUMP,Pump,Pump Pressure Rise
    """

    def __init__(self):
        super().__init__()
        self.flow_temp_setpoint = None

        # WC parameters
        #
        # Chosen by running the load compensated model against a design day
        # with the outside temperatures set at -3 C and 15 C.
        #
        # NOTE: These will need to be recalculated if the radiators are resized.
        self.wc_slope = -1.19
        self.wc_intercept = 46.0

    def set_flow_temp(self, state, t):
        self.api.exchange.set_actuator_value(state, self.flow_temp_setpoint, t)

    def get_val(self, state, handle) -> int:
        return self.api.exchange.get_variable_value(state, handle)

    # This needs to be solved iteratively
    def on_inside_hvac_system_iteration_loop(self, state) -> int:
        if not self.api.exchange.api_data_fully_ready(state):
            return 0

        # TODO: Move this out into another calling point
        if self.flow_temp_setpoint is None:
            print("Using weather compensation")

            # Returns a handle to an input variable.
            #
            # NOTE: These are *output* values of the E+ simulation, as written
            # to eplusout.eso and as such, they must be set as 'Output:Variable's
            # in the .idf file.
            def get_var_handle(var, object):
                handle = self.api.exchange.get_variable_handle(state, var, object)
                assert handle != -1, f"Could not get handle to variable {object}:{var}"
                return handle

            # Returns a handle to an actuator variable (i.e. readable and writable).
            #
            # These are generally control outputs for the simulation.
            def get_act_handle(object_type, object, var):
                handle = self.api.exchange.get_actuator_handle(
                    state, object_type, var, object
                )
                assert handle != -1, (
                    f"Could not get handle to actuator {object_type}{object}:{var}"
                )
                return handle

            try:
                # Inputs:
                self.flow_temp = get_var_handle(
                    "Plant Supply Side Outlet Temperature", "HOT WATER LOOP"
                )
                self.return_temp = get_var_handle(
                    "Heat Pump Load Side Inlet Temperature", "Heat Pump"
                )
                self.flow_rate = get_var_handle("Pump Mass Flow Rate", "SUPPLY PUMP")
                self.outside_temp = get_var_handle(
                    "Site Outdoor Air Drybulb Temperature", "Environment"
                )
                # Outputs:
                self.flow_temp_setpoint = get_act_handle(
                    "Schedule:Constant", "HP Flow Temp Setpoint", "Schedule Value"
                )
                self.flow_rate_setpoint = get_act_handle(
                    "Pump", "SUPPLY PUMP", "Pump Mass Flow Rate"
                )
            except AssertionError as e:
                self.api.runtime.issue_severe(state, str(e))
                return 1

        outside_temp = self.get_val(state, self.outside_temp)
        flow_temp_setpoint = self.wc_slope * outside_temp + self.wc_intercept
        self.set_flow_temp(state, flow_temp_setpoint)

        return 0
