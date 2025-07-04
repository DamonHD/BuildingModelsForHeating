import csv
from statistics import fmean

# Can optionally run the tests through pytest for prettier output,
# if it is available.
try:
    #
    import pytest
except ImportError:
    pass


################################################################################
# Constants and setup
################################################################################
DATA_DIRS = [
    "out-dd-AAAA-LC",
    "out-dd-ABAB-LC",
    "out-dd-AABB-LC",
    "out-dd-AAAA-WC",
    "out-dd-ABAB-WC",
    "out-dd-AABB-WC",
]

CONVERGENCE_ERR = "   ** Warning ** SimHVAC: Maximum iterations (20) exceeded for all HVAC loops, at WINTER DESIGN DAY IN (MID) UK,"
A_ROOM_TEMP_C = 21.0
A_ROOM_SAG_C = 20.0
B_ROOM_TEMP_C = 18.0
Z1_AIR_TEMP = "Z1:Zone Air Temperature [C](Hourly)"
Z2_AIR_TEMP = "Z2:Zone Air Temperature [C](Hourly)"
Z3_AIR_TEMP = "Z3:Zone Air Temperature [C](Hourly)"
Z4_AIR_TEMP = "Z4:Zone Air Temperature [C](Hourly)"
Z1_HEATING_RATE = "Z1 RADIATOR:Baseboard Total Heating Rate [W](Hourly)"
Z2_HEATING_RATE = "Z2 RADIATOR:Baseboard Total Heating Rate [W](Hourly)"
Z3_HEATING_RATE = "Z3 RADIATOR:Baseboard Total Heating Rate [W](Hourly)"
Z4_HEATING_RATE = "Z4 RADIATOR:Baseboard Total Heating Rate [W](Hourly)"
HEAT_PUMP_HEATING_RATE = "HEAT PUMP:Heat Pump Load Side Heat Transfer Rate [W](Hourly)"
WATER_PUMP_HEATING_RATE = "SUPPLY PUMP:Pump Fluid Heat Gain Rate [W](Hourly)"
BASEBOARD_HEATING_RATE = (
    "Baseboard Total Heating Rate All Zones:PythonPlugin:OutputVariable [W](Hourly)"
)
HEAT_PUMP_ELECTRICITY_RATE = "HEAT PUMP:Heat Pump Electricity Rate [W](Hourly)"


def float_near(a, b, err):
    return abs(a - b) < err


def read_eplus_csv(file):
    with open(file) as f:
        output = (
            line[1:]
            for line in csv.reader(
                f,
            )
        )
        return {
            # split into [header, ...values] then parse and average in one step
            column[0].strip(): fmean((float(x) for x in column[1:]))
            # convert to column major representation
            for column in zip(*output)
        }


sim_results = {d: read_eplus_csv(f"{d}/eplusout.csv") for d in DATA_DIRS}

###############################################################################
# Tests
###############################################################################

# Basic Sense Checks
# ==================


def test_converges():
    def has_convergence_error(file):
        with open(file) as f:
            for line in f.readlines():
                if line.startswith(CONVERGENCE_ERR):
                    return line
        return None

    result = ((d, has_convergence_error(f"{d}/eplusout.err")) for d in DATA_DIRS)
    result = [r for r in result if r[1] is not None]

    assert len(result) == 0, result


def test_AAAA_LC_heatflows_balance():
    results = sim_results["out-dd-AAAA-LC"]
    total_heating_supply = (
        results[HEAT_PUMP_HEATING_RATE] + results[WATER_PUMP_HEATING_RATE]
    )
    total_heating_demand = (
        results[Z1_HEATING_RATE]
        + results[Z2_HEATING_RATE]
        + results[Z3_HEATING_RATE]
        + results[Z4_HEATING_RATE]
    )
    total_baseboard_heating_rate = results[BASEBOARD_HEATING_RATE]

    assert float_near(total_heating_demand, total_baseboard_heating_rate, 0.1)
    assert float_near(total_heating_supply, total_heating_demand, 1.0)


def test_AAAA_WC_heatflows_balance():
    results = sim_results["out-dd-AAAA-WC"]
    total_heating_supply = (
        results[HEAT_PUMP_HEATING_RATE] + results[WATER_PUMP_HEATING_RATE]
    )
    total_heating_demand = (
        results[Z1_HEATING_RATE]
        + results[Z2_HEATING_RATE]
        + results[Z3_HEATING_RATE]
        + results[Z4_HEATING_RATE]
    )
    total_baseboard_heating_rate = results[BASEBOARD_HEATING_RATE]

    assert float_near(total_heating_demand, total_baseboard_heating_rate, 0.1)
    assert float_near(total_heating_supply, total_heating_demand, 1.0)


def test_AABB_LC_heatflows_balance():
    results = sim_results["out-dd-AABB-LC"]
    total_heating_supply = (
        results[HEAT_PUMP_HEATING_RATE] + results[WATER_PUMP_HEATING_RATE]
    )
    total_heating_demand = (
        results[Z1_HEATING_RATE]
        + results[Z2_HEATING_RATE]
        + results[Z3_HEATING_RATE]
        + results[Z4_HEATING_RATE]
    )
    total_baseboard_heating_rate = results[BASEBOARD_HEATING_RATE]

    assert float_near(total_heating_demand, total_baseboard_heating_rate, 0.1)
    assert float_near(total_heating_supply, total_heating_demand, 1.0)


def test_AABB_WC_heatflows_balance():
    results = sim_results["out-dd-AABB-WC"]
    total_heating_supply = (
        results[HEAT_PUMP_HEATING_RATE] + results[WATER_PUMP_HEATING_RATE]
    )
    total_heating_demand = (
        results[Z1_HEATING_RATE]
        + results[Z2_HEATING_RATE]
        + results[Z3_HEATING_RATE]
        + results[Z4_HEATING_RATE]
    )
    total_baseboard_heating_rate = results[BASEBOARD_HEATING_RATE]

    assert float_near(total_heating_demand, total_baseboard_heating_rate, 0.1)
    assert float_near(total_heating_supply, total_heating_demand, 1.0)


def test_ABAB_LC_heatflows_balance():
    results = sim_results["out-dd-ABAB-LC"]
    total_heating_supply = (
        results[HEAT_PUMP_HEATING_RATE] + results[WATER_PUMP_HEATING_RATE]
    )
    total_heating_demand = (
        results[Z1_HEATING_RATE]
        + results[Z2_HEATING_RATE]
        + results[Z3_HEATING_RATE]
        + results[Z4_HEATING_RATE]
    )
    total_baseboard_heating_rate = results[BASEBOARD_HEATING_RATE]

    assert float_near(total_heating_demand, total_baseboard_heating_rate, 0.1)
    assert float_near(total_heating_supply, total_heating_demand, 1.0)


def test_ABAB_WC_heatflows_balance():
    results = sim_results["out-dd-ABAB-WC"]
    total_heating_supply = (
        results[HEAT_PUMP_HEATING_RATE] + results[WATER_PUMP_HEATING_RATE]
    )
    total_heating_demand = (
        results[Z1_HEATING_RATE]
        + results[Z2_HEATING_RATE]
        + results[Z3_HEATING_RATE]
        + results[Z4_HEATING_RATE]
    )
    total_baseboard_heating_rate = results[BASEBOARD_HEATING_RATE]

    assert float_near(total_heating_demand, total_baseboard_heating_rate, 0.1)
    assert float_near(total_heating_supply, total_heating_demand, 1.0)


# Room Temperatures
# =================


def test_AAAA_LC_room_temps():
    results = sim_results["out-dd-AAAA-LC"]
    assert float_near(results[Z1_AIR_TEMP], A_ROOM_TEMP_C, 0.01)
    assert float_near(results[Z2_AIR_TEMP], A_ROOM_TEMP_C, 0.01)
    assert float_near(results[Z3_AIR_TEMP], A_ROOM_TEMP_C, 0.01)
    assert float_near(results[Z4_AIR_TEMP], A_ROOM_TEMP_C, 0.01)


def test_AAAA_WC_room_temps():
    results = sim_results["out-dd-AAAA-WC"]
    assert float_near(results[Z1_AIR_TEMP], A_ROOM_TEMP_C, 0.01)
    assert float_near(results[Z2_AIR_TEMP], A_ROOM_TEMP_C, 0.01)
    assert float_near(results[Z3_AIR_TEMP], A_ROOM_TEMP_C, 0.01)
    assert float_near(results[Z4_AIR_TEMP], A_ROOM_TEMP_C, 0.01)


def test_AABB_LC_room_temps():
    results = sim_results["out-dd-AABB-LC"]
    assert float_near(results[Z1_AIR_TEMP], A_ROOM_TEMP_C, 0.01)
    assert float_near(results[Z2_AIR_TEMP], A_ROOM_TEMP_C, 0.01)
    assert float_near(results[Z3_AIR_TEMP], B_ROOM_TEMP_C, 0.01)
    assert float_near(results[Z4_AIR_TEMP], B_ROOM_TEMP_C, 0.01)


def test_AABB_WC_room_temps():
    results = sim_results["out-dd-AABB-WC"]
    assert float_near(results[Z1_AIR_TEMP], A_ROOM_SAG_C, 0.5)
    assert float_near(results[Z2_AIR_TEMP], A_ROOM_SAG_C, 0.5)
    assert float_near(results[Z3_AIR_TEMP], B_ROOM_TEMP_C, 0.01)
    assert float_near(results[Z4_AIR_TEMP], B_ROOM_TEMP_C, 0.01)


def test_ABAB_LC_room_temps():
    results = sim_results["out-dd-ABAB-LC"]
    assert float_near(results[Z1_AIR_TEMP], A_ROOM_TEMP_C, 0.01)
    assert float_near(results[Z2_AIR_TEMP], B_ROOM_TEMP_C, 0.01)
    assert float_near(results[Z3_AIR_TEMP], B_ROOM_TEMP_C, 0.01)
    assert float_near(results[Z4_AIR_TEMP], A_ROOM_TEMP_C, 0.01)


def test_ABAB_WC_room_temps():
    results = sim_results["out-dd-ABAB-WC"]
    assert float_near(results[Z1_AIR_TEMP], A_ROOM_SAG_C, 0.5)
    assert float_near(results[Z2_AIR_TEMP], B_ROOM_TEMP_C, 0.01)
    assert float_near(results[Z3_AIR_TEMP], B_ROOM_TEMP_C, 0.01)
    assert float_near(results[Z4_AIR_TEMP], A_ROOM_SAG_C, 0.5)


# Electricity usage
# =================


def test_LC_energy_usage_ordering():
    aaaa = sim_results["out-dd-AAAA-LC"][HEAT_PUMP_ELECTRICITY_RATE]
    aabb = sim_results["out-dd-AABB-LC"][HEAT_PUMP_ELECTRICITY_RATE]
    abab = sim_results["out-dd-ABAB-LC"][HEAT_PUMP_ELECTRICITY_RATE]

    assert aaaa < aabb < abab


def test_WC_energy_usage_ordering():
    aaaa = sim_results["out-dd-AAAA-WC"][HEAT_PUMP_ELECTRICITY_RATE]
    aabb = sim_results["out-dd-AABB-WC"][HEAT_PUMP_ELECTRICITY_RATE]
    abab = sim_results["out-dd-ABAB-WC"][HEAT_PUMP_ELECTRICITY_RATE]

    assert abab < aaaa
    assert aabb < aaaa


################################################################################
# For running as a self contained script
################################################################################


def dummy():
    pass


if __name__ == "__main__":
    import inspect

    tests = [
        fn
        for fn in inspect.getmembers(inspect.getmodule(dummy), inspect.isfunction)
        if fn[0].startswith("test_")
    ]
    print(f"Running {len(tests)} tests.\n")

    passes = 0
    fails = 0
    for i, (name, test) in enumerate(tests):
        print(f"Running test {i} {name}: ", end="")
        try:
            test()
            passes += 1
            print("PASS")
        except Exception:
            fails += 1
            print("FAIL")

    print(f"\n{passes} tests passed, {fails} tests failed.")
