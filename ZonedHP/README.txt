Various heat-pump with (micro-)zoning models.

Items to note:

  * bungalow-1
    First approximation to the initial bungalow, unzoned AAAA, from DOI 10.3390/su16114710
    As of 20250413-snapshot steady -3C exterior:
        DHD20240413: 'operative' (@0.5) thermostat raises ZONE ONE PURCHASED AIR,Zone Ideal Loads Zone Total Heating Rate [W] to 2025W (cf 3825W at 0.89).
        DHD20240413: now 28.35GJ (7876kWh, 900W) annual for Birmingham weather annual simulation.  (Manchester EGCC from paper 875W.)
 
  * bungalow-1-diurnal
    As bungalow-1/20250413-snapshot but with 3C peak-to-peak diurnal temperature swing. 
        DHD20250508: adjusted Daily Temp Range {C} to 3 (and max to -1.5 to approx preserve mean), for similar range to CIBSE Leeds (UK) typical winter day.
        DHD20250508: ext temperature and Zone Ideal Loads Zone Total Heating Rate [W] range from -4.5C to -1.5C and 1993W and 2188W.

  * bungalow-2
    As bungalow-1 but partitioned into 4 rooms/zones.

  * detached-2
    As bungalow-2 but with an extra level and thus 4 more rooms on top.
 
  * midterrace-2
    As if LHS of detached-2, adiabatic side-walls, and share room/zone numbering.


All of bungalow-1, bungalow-2, detatched-2 and midterrace-2
nominally share the same zone numbering plane and spatial layout,
with only detatched-2 having all 8 zones.


TO-DO / PLAN (2026Q4)

	  * (w/e 20261018) Complete midterrace-2 incl adjusted heat loss for upper vs lower floors
	  * Run design day sim
	  * (w/e 20261025) Tidy, eg location, weather, shared HP model, collate to make running as batch better, eg for other researchers.
	  * (w/e 20261101) Run as annual sim, either with constant weather or not an compared w/ design-day
	  * (w/e 20261108) Add option to add thermal capacity to internal walls and cf DD and annual sims




Useful tools:
  * Online DXF viewer: https://sharecad.org/ (3D Wireframe view was especially revealing with bungalow-2!)