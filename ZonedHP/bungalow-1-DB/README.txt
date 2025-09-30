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
DHD20250926: adjusting walls towards U=0.61; XPS to woodwool@0.1 same 0.08m, U now 0.771 vs 0.351, heat loss 1811W.
DHD20250930: adjusting roof towards U=0.61; MW Glass Wool (rolls)@0.04 to woodwool@0.1 same 0.145m, U now 0.531 vs 0.246.
DHD20250930: adjusting roof towards U=0.61; MW Glass Wool (rolls)@0.04 to Aerated Concrete@0.12 same 0.145m, U now 0.628 vs 0.246.
DHD20250930: adjusting walls towards U=0.61; vegetable fibre board@0.072 same 0.08m, U now 0.622 vs 0.351, heat los ~2200W.

DHD20250930: overriding winter DD ext temp from Birmingham -5.1C to -3C and wind speed to 0.


