The bungalow-2 model, modified to use a heat pump to heat a convective radiator.

Based on `20250623DE-fix-snapshot/bungalow-2.idf`

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


## Unexpected Setback Behaviour

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

## TODO

- [ ] Work out how to correctly model HPs.
  - [ ] Linear COP model from DHD paper
  - [ ] Valliant aroTherm 8 kW
  - [ ] Altherma 3 M (Monobloc) EDLA04E2V3
- [ ] Decide on output parameters.
