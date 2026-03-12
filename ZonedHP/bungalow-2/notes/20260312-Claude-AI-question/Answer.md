# Why the bungalow-2 heat loss isn't exactly 2 kW

**The EnergyPlus bungalow-2 model's design-day heat loss deviates from 2 kW because the 2 kW figure was never a physical calculation — it was an input parameter in a simplified Java model.** Translating that single number into a full EnergyPlus simulation with explicit material layers, dynamic surface physics, ground coupling, and radiative sky exchange introduces at least six independent mechanisms that each push the result away from 2000 W. The DesignBuilder cross-check of the companion bungalow-1 model achieved **~2030 W** at winter design-day conditions, confirming the net effect is a slight overshoot. Understanding why requires tracing the path from the simple model's assumptions to what EnergyPlus actually computes.

## The simple model treats 2 kW as a given, not a result

The bungalow-2 EnergyPlus model descends from the HGTRVHPMModel, a single-class Java model published in the TRVmodel repository and described in Hart-Davis, Liu & Leach (2024). That model defines **HLW = 2000 W** as a compile-time constant — the whole-home heat loss at −3 °C outside, 21 °C inside (ΔT = 24 K). From this it derives a heat-loss coefficient **HLpK = 83.33 W/K** and a uniform envelope U-value **EWRU ≈ 1.13 W/m²K** applied identically to external walls and roof. The floor has zero heat loss. There is no infiltration, no solar gain, no thermal mass, no sky radiation. Every watt of heat loss is fabric conduction, and the total equals 2000 W by definition.

The EnergyPlus bungalow-2 model attempts to reproduce this same building — an 8 × 8 × 2.3 m single-storey bungalow divided into four equal 4 × 4 m rooms — but using a physics engine that cannot accept "2 kW" as an input. Instead, it must build the answer from material conductivities, layer thicknesses, surface areas, boundary conditions, and dynamic heat-balance equations. The gap between the simple model's assumptions and what EnergyPlus actually computes explains the deviation.

## Six mechanisms that move the needle away from 2 kW

### 1. Discrete material layers cannot hit an arbitrary UA product

The simple model requires a total envelope UA of 83.33 W/K distributed across walls and roof. For an 8 × 8 × 2.3 m building, the relevant areas are: external walls **73.6 m²** (4 × 8 × 2.3), flat roof **64 m²**, total **137.6 m²**. To match 83.33 W/K with a uniform U-value, each element needs U = 83.33 / 137.6 = **0.606 W/m²K**. In EnergyPlus, U-values emerge from stacking material layers — each with a specific conductivity, density, specific heat, and thickness drawn from materials databases. Hitting 0.606 W/m²K for both wall and roof constructions simultaneously requires adjusting insulant properties. Hart-Davis notes he achieved "within ~10% of target U-values for roof and walls" by substituting alternative insulants without changing layer thickness. A 10% error in U-value across 137.6 m² at ΔT = 24 K translates to roughly **±200 W** of uncertainty. The DesignBuilder reconstruction started at just ~1145 W before U-value tuning, underscoring how sensitive the total is to construction definitions.

### 2. Ground-coupled floor adds heat loss that should be zero

The simple model assigns exactly zero heat loss to the floor. EnergyPlus cannot replicate this physically. Whether using Foundation:Kiva (a 2D finite-difference ground heat transfer solver), the legacy GroundHeatTransfer:Slab preprocessor, or even simplified monthly ground temperatures via Site:GroundTemperature:BuildingSurface, **the floor always loses some heat to the ground**. Hart-Davis explicitly noted that "~halving the floor U-value (by switching to a better insulating foam in one layer) does not reduce building heat loss" — a signature of ground-coupling physics where the dominant thermal resistance is in the soil, not the slab. With 64 m² of floor over ground whose deep temperature sits around 10–12 °C in the UK, even a well-insulated slab-on-grade typically loses **50–150 W** at design conditions. This is pure addition to the simple model's total.

### 3. Longwave radiation to a cold sky increases roof and wall losses

This is perhaps the most physically significant deviation. EnergyPlus calculates longwave radiative exchange between exterior surfaces and the sky separately from convective exchange. On a clear winter design night at −3 °C outdoor air temperature, the **sky temperature can be 15–25 °C below the air temperature** (roughly −18 to −28 °C), depending on humidity and cloud cover. The Clark & Allen (1978) sky emissivity model, used by default, computes sky emissivity from dewpoint temperature as ε = 0.787 + 0.764 · ln(T_dp/273).

For a **horizontal flat roof** — which this bungalow has — the sky view factor is 1.0, meaning the entire roof radiates to that cold sky. The radiative heat flux from a roof surface at, say, 5 °C to a sky at −20 °C is substantially greater than what a simple U × A × (21 − (−3)) calculation captures. For vertical walls, the sky view factor drops to ~0.5, halving but not eliminating the effect. Across the 64 m² roof and 73.6 m² of walls, this mechanism can add **100–300 W** beyond the simple conduction estimate, pushing total heat loss above 2 kW.

### 4. Dynamic surface film coefficients differ from standard U-value assumptions

Standard U-values embed fixed internal and external surface resistances (R_si = 0.13 m²K/W, R_so = 0.04 m²K/W per BS EN ISO 6946). EnergyPlus replaces these with dynamic calculations. The default TARP or DOE-2 exterior convection algorithm computes separate forced convection (wind-driven, using Sparrow flat-plate correlations) and natural convection (buoyancy-driven) components at every timestep. At a design-day wind speed of, say, 3.3 m/s, the exterior convection coefficient might range from **10–20 W/m²K** depending on surface roughness and orientation — different from the ~25 W/m²K often embedded in standard external film resistance. If the effective exterior film resistance is higher than assumed in the target U-value, the actual surface-to-air heat transfer decreases (pushing heat loss slightly down). If lower, it increases. The net effect depends on the specific wind speed, surface roughness category, and convection algorithm selected in the IDF.

### 5. Design-day simulation is dynamic, not steady-state

EnergyPlus does not perform a simple steady-state calculation even on a design day. The SizingPeriod:DesignDay object generates a full **24-hour diurnal outdoor temperature profile** using ASHRAE HOF multipliers. The minimum temperature (−3 °C in this case) typically occurs around 5:00 AM, with a warmer daytime peak determined by the daily range parameter. EnergyPlus runs this 24-hour profile repeatedly through a warmup cycle (minimum ~6 days) until zone temperatures converge, then reports the **peak heating load** — the maximum instantaneous load during that converged day.

The Conduction Transfer Function (CTF) method used for wall and roof conduction captures **thermal mass effects**. During the hours before the temperature minimum, heat stored in the building fabric continues to flow outward; during warming hours, the fabric absorbs some heat, reducing the peak load. For a lightweight bungalow with thin walls, thermal mass effects are modest (perhaps ±20–50 W on peak load), but they ensure the result differs from a pure U × A × ΔT calculation using the minimum temperature.

### 6. Infiltration adds ventilation losses absent from the simple model

The simple Java model includes **no infiltration or ventilation** — all heat loss is fabric conduction. If the EnergyPlus bungalow-2 includes even a modest ZoneInfiltration:DesignFlowRate object (which is standard practice in EnergyPlus modelling), this adds a ventilation heat loss term:

**Q_inf = ρ × c_p × V̇ × ΔT**

For a reasonably airtight building at 0.3 ACH (air changes per hour) with zone volume 4 × 64 × 2.3 ≈ 147 m³ (or ~37 m³ per zone): V̇ = 0.3 × 147 / 3600 = 0.0123 m³/s. At ρ ≈ 1.25 kg/m³, c_p = 1005 J/kg·K, ΔT = 24 K: **Q_inf ≈ 370 W**. Even at a very low 0.1 ACH, this adds ~120 W. If infiltration is set to zero in the IDF, this pathway vanishes — but the earth.org.uk documentation does not confirm this for bungalow-2, and standard EnergyPlus practice includes some infiltration.

## Quantifying the combined effect

The DesignBuilder reconstruction of the companion bungalow-1 model (single-zone version of the same building) achieved **~2030 W at winter design-day conditions** — roughly 1.5% above the 2 kW target. Hart-Davis described this as "close enough" and planned to transplant the calibrated constructions into bungalow-2. The table below estimates how each mechanism contributes:

| Mechanism | Likely direction | Estimated magnitude |
|-----------|-----------------|-------------------|
| U-value approximation from discrete layers | ± (depends on tuning) | ±0–200 W |
| Ground-coupled floor (should be zero) | Increases loss | +50–150 W |
| Sky longwave radiation (roof + walls) | Increases loss | +100–300 W |
| Dynamic film coefficients | ± (wind-dependent) | ±20–80 W |
| Thermal mass / diurnal profile | Typically reduces peak | −20–50 W |
| Infiltration (if included) | Increases loss | +0–370 W |
| Solar gains on design day | Reduces loss | −0–50 W |

These effects do not simply add because the EnergyPlus heat balance couples them. The exterior surface temperature depends simultaneously on conduction, convection, and radiation; changing one changes the others. Nevertheless, the dominant upward pressures — ground coupling and sky radiation — likely outweigh downward pressures from thermal mass and solar gain, consistent with the observed ~2030 W result being slightly above target.

## The deeper issue is one of model translation

The fundamental reason the heat loss is not exactly 2 kW is epistemological, not numerical. The simple model defines a building by its aggregate heat-loss coefficient and derives everything else. EnergyPlus defines a building by its physical components and derives the heat-loss coefficient. These are inverse problems, and the mapping between them is not bijective. When you specify material layers to approximate a target U-value, you simultaneously introduce thermal mass, spectral surface properties, and construction-specific film resistances that the simple model never considered. When you place that construction on a simulated earth with a simulated sky, you activate heat-transfer pathways the simple model assumed away. The ~30 W overshoot in the DesignBuilder version represents the cumulative signature of physics that a one-line equation deliberately ignores — and that is precisely the point of moving from a simple model to EnergyPlus.

## Conclusion

The bungalow-2 model's design-day heat loss exceeds 2 kW primarily because the 2 kW was defined as a boundary condition in a simplified model, not as an emergent property of a physically specified building. Three factors dominate the deviation: **ground-coupled floor losses** (which cannot be zeroed out in EnergyPlus), **longwave radiation to a sky much colder than the outdoor air** (especially punishing for the flat roof with its sky view factor of 1.0), and the **impossibility of perfectly matching a target UA product using discrete material layers**. Infiltration, if included, would further widen the gap. The DesignBuilder cross-check landing at ~2030 W confirms these effects are collectively modest — about +1.5% — but they are physically real and irreducible consequences of upgrading from a lumped-parameter model to a dynamic building energy simulation.