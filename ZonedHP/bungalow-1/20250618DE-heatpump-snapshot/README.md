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

## COP

I'm not exactly sure what the right way of doing this calculation is,
but the Energy Meters Report[^3] seems the most promising.
The following annual and peak values seem relevant to the calculation: 

- `Electricity:Plant`: the electricity usage by the heating plant loop.
- `Heating:Electricity`: the electricity usage by the heating system,
   excluding the water pump.
- `HeatPump:Heating:Electricity`: the electricity usage by just the heat pump.
- `General:Heating:EnergyTransfer`: the heat transfer into the building
  from just the heating system.
- `General:Heating:EnergyTransfer:Zone:*`: the heat transfer into each zone
  from just the heating system.
- `EnergyTransfer:Plant`: Energy transfer by the plant. I'm not entirely sure
   why this is different to `General:Heating:EnergyTransfer`. See [^4].

I'm choosing to calculate the COP in the following way as this seems to be
the most consistent in terms of naming, but we may have to revise it.

```
  COP[max. W] = Electricity:Plant[max. W] / EnergyTransfer:Plant[max. W]
  3.4 = 3185 / 938
```

[^3]: out-dd/eplustbl.htm#EnergyMeters::EntireFacility
[^4]: https://bigladdersoftware.com/epx/docs/8-3/output-details-and-examples/eplusout.mdd.html#additional-end-use-types-only-used-for-energytransfer

## TODO

- [ ] Understand Radiator U-Factor Times Area Value.
- [ ] Understand `PlantEquipmentOperation:HeatingLoad`
- [ ] Work out how to correctly model HPs.
  - [ ] Linear COP model from DHD paper
  - [ ] Valliant aroTherm 8 kW
  - [ ] Altherma 3 M (Monobloc) EDLA04E2V3
- [ ] Decide on output parameters.
