A run with the following settings, and WeatherCompHeatPumpController recalibrated:
- Convection model: TARP
- Roof: New roof
- Temperature control: Operative

| variable         | location   |   aaaa-lc |   aaaa-wc |   aabb-lc |   aabb-wc |   abab-lc |   abab-wc |
|:-----------------|:-----------|----------:|----------:|----------:|----------:|----------:|----------:|
| air_temp_c       | outdoor    |     -3.00 |     -3.00 |     -3.00 |     -3.00 |     -3.00 |     -3.00 |
| air_temp_c       | z1         |     21.00 |     20.96 |     21.00 |     20.51 |     21.00 |     20.37 |
| air_temp_c       | z2         |     21.00 |     20.96 |     21.00 |     20.51 |     19.57 |     19.70 |
| air_temp_c       | z3         |     21.00 |     20.96 |     19.67 |     19.73 |     19.57 |     19.70 |
| air_temp_c       | z4         |     21.00 |     20.96 |     19.67 |     19.73 |     21.00 |     20.37 |
| operative_temp_c | z1         |     19.14 |     19.10 |     19.01 |     18.59 |     18.92 |     18.43 |
| operative_temp_c | z2         |     19.14 |     19.10 |     19.01 |     18.59 |     18.00 |     18.00 |
| operative_temp_c | z3         |     19.14 |     19.10 |     18.00 |     18.00 |     18.00 |     18.00 |
| operative_temp_c | z4         |     19.14 |     19.10 |     18.00 |     18.00 |     18.92 |     18.43 |
| rad_power_w      | z1         |    473.42 |    472.56 |    498.09 |    479.53 |    514.51 |    481.77 |
| rad_power_w      | z2         |    473.42 |    472.56 |    498.09 |    479.53 |    407.95 |    431.97 |
| rad_power_w      | z3         |    473.42 |    472.56 |    425.88 |    437.09 |    407.95 |    431.97 |
| rad_power_w      | z4         |    473.42 |    472.56 |    425.88 |    437.09 |    514.51 |    481.77 |
| rad_power_w      | total      |   1893.70 |   1890.24 |   1847.94 |   1833.24 |   1844.93 |   1827.48 |
| mass_flow_kgps   | z1         |      0.03 |      0.03 |      0.03 |      0.03 |      0.03 |      0.03 |
| mass_flow_kgps   | z2         |      0.03 |      0.03 |      0.03 |      0.03 |      0.01 |      0.01 |
| mass_flow_kgps   | z3         |      0.03 |      0.03 |      0.01 |      0.01 |      0.01 |      0.01 |
| mass_flow_kgps   | z4         |      0.03 |      0.03 |      0.01 |      0.01 |      0.03 |      0.03 |
| mass_flow_kgps   | water_pump |      0.13 |      0.13 |      0.13 |      0.13 |      0.13 |      0.13 |
| flow_temp_c      | heat_pump  |     51.36 |     51.27 |     52.95 |     51.27 |     54.00 |     51.27 |
| return_temp_c    | heat_pump  |     47.88 |     47.80 |     49.55 |     47.90 |     50.61 |     47.91 |
| heat_gain_w      | heat_pump  |   1891.30 |   1887.84 |   1845.40 |   1830.86 |   1842.37 |   1825.10 |
| heat_gain_w      | water_pump |      1.97 |      1.97 |      1.97 |      1.97 |      1.97 |      1.97 |
| heat_gain_w      | total      |   1893.27 |   1889.81 |   1847.38 |   1832.84 |   1844.34 |   1827.07 |
| electricity_w    | heat_pump  |    819.80 |    816.66 |    826.57 |    792.02 |    842.87 |    789.53 |
| electricity_w    | water_pump |      1.97 |      1.97 |      1.97 |      1.97 |      1.97 |      1.97 |
| electricity_w    | total      |    821.77 |    818.64 |    828.54 |    793.99 |    844.84 |    791.50 |
| COP (H4)         | total      |      2.30 |      2.31 |      2.23 |      2.31 |      2.18 |      2.31 |
