The bungalow-2 model, modified to use a heat pump to heat a convective radiator.

Based on `20250623DE-fix-snapshot/bungalow-2.idf`

# Heating Model

A simple single room, single zone hot water heating loop.

- Heat Pump set point: 55 C
- Zone set point: 21 C
- Heating Rate per rad \[W](Hourly): 444.5
- Total Heating Rate \[W](Hourly): 1778

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

## TODO

- [ ] Work out how to correctly model HPs.
  - [ ] Linear COP model from DHD paper
  - [ ] Valliant aroTherm 8 kW
  - [ ] Altherma 3 M (Monobloc) EDLA04E2V3
- [ ] Decide on output parameters.
