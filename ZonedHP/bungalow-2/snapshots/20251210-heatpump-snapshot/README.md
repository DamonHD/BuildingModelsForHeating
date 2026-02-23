The bungalow-2 model, modified to use a heat pump to heat a convective radiator.

Based on `20250625DE-heatpump-snapshot/bungalow-2-heatpump.idf`

# Heating Model

A four zone, four radiator model heated by a heat pump.

The heatpump flow temperature setpoint is modulated by a proportional control
in order provide enough heat to keep Zone 1 at 21 C (load compensation).

This model demonstrates bad setback effects.

- "A" Zone room set point: 21 C
- "B" Zone room set point: 18 C

```
                  +-----+-------------+------+------------+------------+------------+
                  |     |Supply       |      |            |            |            |
                  |     |Bypass       |      v            v            v            v
+---------+   +---+--+  |             | +----------+ +----------+ +----------+ +----------+
|         |<--+      |  |             | |          | |          | |          | |          |
| Outside |   | Heat |  |             | | Radiator | | Radiator | | Radiator | | Radiator |
|   Air   |   | Pump |  |       Demand| |          | |          | |          | |          |
|         +-->|      |  |       Bypass| +----+-----+ +----+-----+ +----+-----+ +----+-----+
+---------+   +------+  |             |      |            |            |            | 
                  ^     |  +------+   |      |            |            |            |  
                  |     |  |      |   |      |            |            |            | 
                  +-----+--+ Pump |<--+------+------------+------------+------------+
                           |      |                 
                           +------+                 
```

# Results Summary

| variable       | location   |    aaaa |    aabb |    abab |
|:---------------|:-----------|--------:|--------:|--------:|
| air_temp_c     | outdoor    |   -3.00 |   -3.00 |   -3.00 |
|                | z1         |   21.00 |   21.00 |   21.00 |
|                | z2         |   21.00 |   21.00 |   18.00 |
|                | z3         |   21.00 |   18.00 |   18.00 |
|                | z4         |   21.00 |   18.00 |   21.00 |
| rad_power_w    | z1         |  444.33 |  498.06 |  520.34 |
|                | z2         |  444.33 |  498.06 |  312.74 |
|                | z3         |  444.33 |  335.02 |  312.74 |
|                | z4         |  444.33 |  335.02 |  520.34 |
|                | total      | 1777.33 | 1666.18 | 1666.17 |
| mass_flow_kgps | z1         |    0.03 |    0.03 |    0.03 |
|                | z2         |    0.03 |    0.03 |    0.00 |
|                | z3         |    0.03 |    0.00 |    0.00 |
|                | z4         |    0.03 |    0.00 |    0.03 |
|                | water_pump |    0.13 |    0.13 |    0.13 |
| flow_temp_c    | heat_pump  |   45.02 |   47.90 |   49.11 |
| return_temp_c  | heat_pump  |   41.75 |   44.84 |   46.04 |
| heat_gain_w    | heat_pump  | 1775.36 | 1663.98 | 1663.97 |
|                | water_pump |    1.97 |    1.97 |    1.97 |
|                | total      | 1777.32 | 1665.95 | 1665.94 |
| electricity_w  | heat_pump  |  666.77 |  668.74 |  686.97 |
|                | water_pump |    1.97 |    1.97 |    1.97 |
|                | total      |  668.73 |  670.71 |  688.94 |
| COP (H4)       | total      |    2.66 |    2.48 |    2.42 |

# DENotes

## Heat Pump

There are several options for simulating an air to water source heat pump,
but the docs are unclear on how to choose, and I couldn't find anything helpful
on unmethours.

The `HeatPump:PlantLoop:EIR:Heating` model seems like the most direct option,
so I went with that.

## Heat Transfer Discrepancy

The `HeatPump:PlantLoop:EIR:Heating` provides the `Heat Pump Load Side Heat Transfer Rate` output, 
which I think is the heat transfered from the heatpump to the hot water loop in W.
The peak value is `~1680 W`, but the peak radiator ouput power is `~444.5 * 4 = 1778 W`.

I'm not sure if this is a problem with the model, a bug in E+,
or just me not understanding the model/outputs.


## ~~Unexpected Setback Behaviour~~

With some rooms set back to 18 C, I would expect the warm rooms
to be slightly below or at their setpoints, and the cool rooms
to be slightly above their setpoints.
Additionally, the bad setback model predicts that electricity usage
should be higher.

Neither of these is true for the current model.

| variable      | location   | aaaa   | aabb   | abab   |
|--------------:|-----------:|-------:|-------:|-------:|
| air_temp_c    | z1         |   21.0 |   21.7 |   22.2 |
|               | z2         |   21.0 |   21.7 |   16.8 |
|               | z3         |   21.0 |   17.3 |   16.8 |
|               | z4         |   21.0 |   17.3 |   22.2 |
| electricity_w | total      |  588.3 |  556.6 |  556.6 |
| power_w       | heat_pump  | 1679.8 | 1568.7 | 1568.7 |
| rad_power_w   | total      | 1777.3 | 1666.2 | 1666.2 |
|               | z1         |  444.3 |  535.9 |  604.8 |
|               | z2         |  444.3 |  535.9 |  228.3 |
|               | z3         |  444.3 |  297.2 |  228.3 |
|               | z4         |  444.3 |  297.2 |  604.8 |

RESOLUTION:

This was due to using `Thermostat:OperativeTemperature` model
for the zone thermostats, while using just the dry bulb temperature for
the reported zone temperatures.
I've changed the thermostat to be based on the dry bulb temperature for now,
which is also more consistent with only using a convective radiator model.

## Radiator Sizing

- Was not seeing any temperature sag in A rooms
- Fixed max flow rates in the system
- Heating design capacity doesn't seem to do anything
- ~~Only working sizing parameter seems to be U-Factor Times Area Value (UA)~~
- Now works as expected
- Added it to the template as an adjustable param
- With the addition of load compensation:
  - Max rad flowrates had to be limited.
  - UA had to be increased to reduce flow temperatures from max.

### ~~Hot Water Loop Mass Flow and Heat Flow Balancing Issues~~

Undersized rads cause the model to fail to converge, resulting in
the rads in the A rooms using the full PlantLoop max water flow rate each,
and the demand side using about double the heating power that the heat pump
is providing.

RESOLUTION:

Reducing the max flow rate setting on the radiators fixed this issue.
