The bungalow-2 model, modified to use a heat pump to heat a convective radiator.

Based on `20250625DE-heatpump-snapshot/bungalow-2-heatpump.idf`

# Heating Model

A simple single room, single zone hot water heating loop.

- Heat Pump set point: 55 C
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

| variable      | location   | aaaa    | aabb    | abab    |
|---------------|------------|--------:|--------:|--------:|
| air_temp_c    | z1         |   20.6  |   19.7  |   19.4  |
|               | z2         |   20.6  |   19.7  |   18.0  |
|               | z3         |   20.6  |   18.0  |   18.0  |
|               | z4         |   20.6  |   18.0  |   19.4  |
| rad_power_w   | z1         |  437.1  |  449.2  |  452.0  |
|               | z2         |  437.1  |  449.2  |  352.2  |
|               | z3         |  437.1  |  359.1  |  352.2  |
|               | z4         |  437.1  |  359.1  |  452.0  |
|               | total      | 1748.5  | 1616.6  | 1608.5  |
| electricity_w | heat_pump  |  246.8  |  460.7  |  458.4  |
|               | water_pump |    3.8  |    4.0  |    4.0  |
|               | total      |  250.6  |  464.7  |  462.4  |
| heat_gain_w   | heat_pump  |  863.8  | 1612.3  | 1604.2  |
|               | water_pump |    3.8  |    4.0  |    4.0  |
|               | total      |  867.7  | 1616.3  | 1608.3  |
| COP (H4)      | total      |    3.46 |    3.48 |    3.48 |

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
- Only working sizing parameter seems to be U-Factor Times Area Value
- Now works as expected
- Added it to the template as an adjustable param, currently set to 13.35

### ~~Hot Water Loop Mass Flow and Heat Flow Balancing Issues~~

Undersized rads cause the model to fail to converge, resulting in
the rads in the A rooms using the full PlantLoop max water flow rate each,
and the demand side using about double the heating power that the heat pump
is providing.

RESOLUTION:

Reducing the max flow rate setting on the radiators fixed this issue.

## TODO

- [ ] Work out how to correctly model HPs.
  - [ ] Linear COP model from DHD paper
  - [ ] Valliant aroTherm 8 kW
  - [ ] Altherma 3 M (Monobloc) EDLA04E2V3
- [ ] Decide on output parameters.
