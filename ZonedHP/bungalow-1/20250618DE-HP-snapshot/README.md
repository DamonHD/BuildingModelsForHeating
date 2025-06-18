The bungalow-1 model, modified to use a heat pump to heat a convective radiator.

# Heating Model

A simple single room, single zone hot water heating loop.

- Heat Pump set point: 55 C
- Zone set point: 21 C
- Total Heating Rate \[W](Hourly): 2006

```
                  +-----+-------------+------+      
                  |     |Supply       |      |      
                  |     |Bypass       |      v      
+---------+   +---+--+  |             | +----------+
|         |<--+      |  |             | |          |
| Outside |   | Heat |  |             | | Radiator |
|   Air   |   | Pump |  |       Demand| |          |
|         +-->|      |  |       Bypass| +----+-----+
+---------+   +------+  |             |      |      
                  ^     |  +------+   |      |      
                  |     |  |      |   |      |      
                  +-----+--+ Pump |<--+------+      
                           |      |                 
                           +------+                 
```
# DENotes

## Radiator

I tried to configure the radiator according to [^1] and [^2],
but I'm not exactly sure what the `U-Factor Times Area Value` is yet.
Solving `q = UA x (Twater - Tair)` for `UA` gives a very low value
when using `q = radW' and '(Twater - Tair) = radMWATdT`, so I set the value
to something that matches the performance of the baseline model (`20250413-snapshot`).

[^1]: https://www.mdpi.com/2071-1050/16/11/4710
[^2]: https://bigladdersoftware.com/epx/docs/22-2/input-output-reference/group-radiative-convective-units.html#zonehvacbaseboardconvectivewater

## Heat Pump

There are several options for simulating an air to water source heat pump,
but the docs are unclear on how to choose, and I couldn't find anything helpful
on unmethours.

The `HeatPump:PlantLoop:EIR:Heating` model seems like the most direct option,
so I went with that.

## TODO

- [ ] Understand Radiator U-Factor Times Area Value.
- [ ] Understand `PlantEquipmentOperation:HeatingLoad`
- [ ] Work out how to correctly model HPs.
  - [ ] Linear COP model from DHD paper
  - [ ] Valliant aroTherm 8 kW
  - [ ] Altherma 3 M (Monobloc) EDLA04E2V3
- [ ] Decide on output parameters.
