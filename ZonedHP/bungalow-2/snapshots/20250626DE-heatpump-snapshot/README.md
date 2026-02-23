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

### ABAB With Undersized Radiator

| variable      | location   | aaaa   | aabb   | abab   |
|--------------:|-----------:|-------:|-------:|-------:|
| air_temp_c    | z1         |   21.0 |   20.0 |   19.7 |
|               | z2         |   21.0 |   20.0 |   18.0 |
|               | z3         |   21.0 |   18.0 |   18.0 |
|               | z4         |   21.0 |   18.0 |   19.7 |
| electricity_w | total      |  514.1 |  227.8 |  229.2 |
| power_w       | heat_pump  | 1769.4 |  778.3 |  784.2 |
| rad_power_w   | total      | 1777.3 | 1628.1 | 1618.5 |
|               | z1         |  444.3 |  460.6 |  463.9 |
|               | z2         |  444.3 |  460.6 |  345.3 |
|               | z3         |  444.3 |  353.4 |  345.3 |
|               | z4         |  444.3 |  353.4 |  463.9 |

## TODO

- [ ] Work out how to correctly model HPs.
  - [ ] Linear COP model from DHD paper
  - [ ] Valliant aroTherm 8 kW
  - [ ] Altherma 3 M (Monobloc) EDLA04E2V3
- [ ] Decide on output parameters.
