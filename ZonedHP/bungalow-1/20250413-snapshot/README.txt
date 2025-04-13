First approximation to the initial bungalow, unzoned AAAA, from DOI 10.3390/su16114710
To Zone or Not to Zone When Upgrading a Wet Heating System from Gas to Heat Pump for Maximum Climate Impact: A UK View
Hart-Davis, Damon and Liu, Lirong and Leach, Matthew
MDPI Sustainability 2024
https://www.mdpi.com/2071-1050/16/11/4710

This is designed to run in EnergyPlus V24.2 or newer.

! Some features of 10.3390/su16114710 bungalow, mid-UK / Salford EH1 / Birmingham weather.
! NOTE: Salford location and design day lines copied in from EH1 model.
!
! hart-davis2024zone bungalow parameters:
!     IWL (Internal Wall Length) = 4m, thus whole external wall length 8m.
!     IWH (Internal Wall Height) = 2.3m
!     EWRU (Effective Wall and Roof U-value): 0.61 W/m2K
!     Wall and roof surface: (4x18.4m2 + 64m2) 137.6m2
!     Floor non-conducting
!     Interior and exterior temperatures at design conditions: 21C / -3C
!     Expected heat demand at design conditions: 2000W
!
! Building: Fictional 1 zone building with resistive walls and flat roof.
!
! The building is oriented due north.
!
! Floor Area:        64 m2
! No internal walls / partitions.
! Number of Stories: 1
! Computed effective wall and roof U value (EWRU): 0.61 W/m2K

! Acknowledgements:
!
! DERIVED FROM EH1 fragments with permission, and EnergyPlus shipped files:
!     Minimal.idf Example1A.idf 1ZoneUncontrolled.idf
!
! See https://energyplus.readthedocs.io/en/latest/acknowledgments/acknowledgments.html
! NOTICE: The U.S. Government is granted for itself and others acting on its behalf a paid-up, nonexclusive, irrevocable, worldwide license in this data to reproduce, prepare derivative works, and perform publicly and display publicly. Beginning five (5) years after permission to assert copyright is granted, subject to two possible five year renewals, the U.S. Government is granted for itself and others acting on its behalf a paid-up, non-exclusive, irrevocable worldwide license in this data to reproduce, prepare derivative works, distribute copies to the public, perform publicly and display publicly, and to permit others to do so.

Note that GB weather files are available from:
    https://energyplus.net/weather-region/europe_wmo_region_6/GBR
The licence does not apparently allow redistribution:
    https://energyplus.net/assets/nrel_custom/weather/ashrae_license_agreement.txt

Note that Construction CTF shows U-value (ThermalConductance) for each construction.

Some basics of the IDF file:
    https://bigladdersoftware.com/epx/docs/9-2/input-output-reference/group-simulation-parameters.html
    

NOTES
=====

DHD20250322: Total Site Energy now 15.76GJ (at 21C heat setpoint), was 11.44GJ.
DHD20250322: TSE at 24.96GJ once ground temperatures updated.
DHD20250322: TSE at 16.68GJ once floor made near lossless.
DHD20250322: added EH1 shallow and deep ground temps: no TSE change.
DHD20250330: adjusted STDEWR so Construction CTF shows U-value (ThermalConductance) EWRU of 0.61W/m2K.
DHD20250330: roof and walls now STDEWR: TSE now 21.94GJ (6094kWh, ~696W), vs paper's London EGLL 2018 AAAA 719W.
DHD20250331: adjusted terrain to Suburbs (from Country) and TSE fell marginally to 21.72GJ.
DHD20250401: Annual and Peak Values - Other -> (eg) Heating:EnergyTransfer max on 15 Jan is 1520.92W.
DHD20250401: adjusted winter DD to 'UK' -3C, no wind, Heating:EnergyTransfer max on 15 Jan is 1309.69W.
DHD20250401: simplified wall/roof to one layer, Heating:EnergyTransfer max on 15 Jan is 1400.14W.
DHD20250401: roof set to Surface Type 'Wall' for same film coefficients as walls: U-Factor with Film now 0.61W/m2K.
DHD20250401: manual calc of heat demand suggests 2014W, not 1400W!  (Ext -3C, int 21C, 137.6m^2 @ 0.61W/m2K.)
DHD20250401: TSE now 23.31GJ (6475kWh, ~739W), vs paper's London EGLL 2018 AAAA 719W.
DHD20250407: added extra/final 'Yes' to SimulationControl to try to enable zone sizing.
DHD20250407: read: https://unmethours.com/question/13245/energyplus-output-of-heat-load/
DHD20250407: added to variables output to eplusout.eso Zone Predicted Sensible Load to Setpoint Heat Transfer Rate [W] (shows 1400W winter dd),]
DHD20250407: Zone Air System Sensible Heating Energy [J] agrees with above.
DHD20250407: Also ZONE ONE PURCHASED AIR,Zone Ideal Loads Zone Total Heating Rate [W].
DHD20250407: verified no solar gains with: Surface Outside Face Solar Radiation Heat Gain Rate [W].
DHD20250407: surface heat losses: Surface Average Face Conduction Heat Transfer Rate [W]: 4x183+667 winter dd vs expected 4x269+936.
DHD20250407: trying Output:Table:SummaryReports,AllSummaryAndSizingPeriod vs AllSummary.
DHD20250407: asked https://unmethours.com/question/101466/unexpected-design-day-heat-flows-vs-u-values-in-simple-building/
DHD20250410: UnmetHours comment suggests eg Surface Convection Algorithm:Inside "Simple" (vs "TARP") and Surface Convection Algorithm:Outside "SimpleCombined" (vs "TARP").
DHD20250413: above Surface Convection Algorithm changes raise heat loss to ~1800W.
DHD20250413: note: surface convective heat transfer coefficient = CHTC
DHD20250413: inside and outside surface temperatures are significantly different to expected (eg 17C/-2C), maybe explaining heat low demand.
DHD20240413: 'operative' (@0.5) thermostat raises ZONE ONE PURCHASED AIR,Zone Ideal Loads Zone Total Heating Rate [W] to 2025W (cf 3825W at 0.89).
DHD20240413: now 28.35GJ (7876kWh, 900W) annual for Birmingham weather annual simulation.  (Manchester EGCC from paper 875W.)