Recreating bungalow-1 from scratch in DesignBuilder.
Will require a DB licence to read the .dsb files.
Some versions may be exported as EnergyPlus files: eg .idf 

Working on moving values in "HeatTransfer Surface" (HTML) table to match paper.
HeatTransfer target U values: floor 0, walls/roof with film 0.61 W/m2K.

2025-09-16:
Building now has approx correct external dimensions and character (no windows).
U values are better than needed for bungalow-1,
so design-day heat demand seen in out-3mod-dd/eplusout.eso is ~1146W 
lower than the target 2kW.
230,1,BLOCK1:ZONE1 IDEAL LOADS AIR,Zone Ideal Loads Supply Air Total Heating Rate [W] !TimeStep
...
230,1145.9117657398529



DHD20250926: reverting/updating to 20250916 snapshot with correct exterior; U-values far too good though. 
DHD20250926: minor re-adjustments to target temperatures for nth time (to be 21C/18C).
DHD20250926: changed floor to use PUR@0.026W/mK; layer still 0.133m, floor U now 0.171 vs 0.247, heat loss still ~1145W.
DHD20250906: adjusting walls towards U.61; XPS to woodwool@0.1 same 0.08m, walls U now 0.771 vs 0.351, heat loss 1811W.