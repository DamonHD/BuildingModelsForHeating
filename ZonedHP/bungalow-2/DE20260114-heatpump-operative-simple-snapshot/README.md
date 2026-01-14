A run with the following settings, and WeatherCompHeatPumpController recalibrated:
- Convection model: Simple/SimpleCombined
- Roof: New roof
- Temperature control: Operative

| variable         | location   |   aaaa-lc |   aaaa-wc |   aabb-lc |   aabb-wc |   abab-lc |   abab-wc |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|----------:|----------:|
| air_temp_c       | outdoor    |     -3.00 |     -3.00 |     -3.00 |     -3.00 |     -3.00 |     -3.00 |
| air_temp_c       | z1         |     21.00 |     21.00 |     21.00 |     20.10 |     20.83 |     19.80 |
| air_temp_c       | z2         |     21.00 |     21.00 |     21.00 |     20.10 |     18.40 |     18.59 |
| air_temp_c       | z3         |     21.00 |     21.00 |     18.54 |     18.64 |     18.40 |     18.59 |
| air_temp_c       | z4         |     21.00 |     21.00 |     18.54 |     18.64 |     20.83 |     19.80 |
| operative_temp_c | z1         |     20.13 |     20.14 |     19.91 |     19.13 |     19.61 |     18.80 |
| operative_temp_c | z2         |     20.13 |     20.14 |     19.91 |     19.13 |     18.00 |     18.00 |
| operative_temp_c | z3         |     20.13 |     20.14 |     18.00 |     18.00 |     18.00 |     18.00 |
| operative_temp_c | z4         |     20.13 |     20.14 |     18.00 |     18.00 |     19.61 |     18.80 |
| rad_power_w      | z1         |    452.59 |    452.51 |    505.14 |    466.63 |    532.69 |    471.26 |
| rad_power_w      | z2         |    452.59 |    452.51 |    505.14 |    466.63 |    320.00 |    365.54 |
| rad_power_w      | z3         |    452.59 |    452.51 |    353.36 |    376.68 |    320.00 |    365.54 |
| rad_power_w      | z4         |    452.59 |    452.51 |    353.36 |    376.68 |    532.69 |    471.26 |
| rad_power_w      | total      |   1810.36 |   1810.02 |   1716.99 |   1686.62 |   1705.38 |   1673.60 |
| mass_flow_kgps   | z1         |      0.03 |      0.03 |      0.03 |      0.03 |      0.03 |      0.03 |
| mass_flow_kgps   | z2         |      0.03 |      0.03 |      0.03 |      0.03 |      0.00 |      0.01 |
| mass_flow_kgps   | z3         |      0.03 |      0.03 |      0.00 |      0.01 |      0.00 |      0.01 |
| mass_flow_kgps   | z4         |      0.03 |      0.03 |      0.00 |      0.01 |      0.03 |      0.03 |
| mass_flow_kgps   | water_pump |      0.13 |      0.13 |      0.13 |      0.13 |      0.13 |      0.13 |
| flow_temp_c      | heat_pump  |     50.03 |     50.03 |     53.40 |     50.03 |     55.00 |     50.03 |
| return_temp_c    | heat_pump  |     46.70 |     46.70 |     50.25 |     46.93 |     51.87 |     46.95 |
| heat_gain_w      | heat_pump  |   1808.11 |   1807.76 |   1714.50 |   1684.40 |   1702.89 |   1671.38 |
| heat_gain_w      | water_pump |      1.97 |      1.97 |      1.97 |      1.97 |      1.98 |      1.97 |
| heat_gain_w      | total      |   1810.08 |   1809.73 |   1716.47 |   1686.37 |   1704.87 |   1673.35 |
| electricity_w    | heat_pump  |    761.72 |    761.58 |    774.99 |    709.61 |    794.58 |    704.13 |
| electricity_w    | water_pump |      1.97 |      1.97 |      1.97 |      1.97 |      1.98 |      1.97 |
| electricity_w    | total      |    763.69 |    763.55 |    776.97 |    711.58 |    796.56 |    706.10 |
| COP (H4)         | total      |      2.37 |      2.37 |      2.21 |      2.37 |      2.14 |      2.37 |
