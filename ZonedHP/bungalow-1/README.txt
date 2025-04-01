First approximation to the initial bungalow, unzoned AAAA, from DOI 10.3390/su16114710
To Zone or Not to Zone When Upgrading a Wet Heating System from Gas to Heat Pump for Maximum Climate Impact: A UK View
Hart-Davis, Damon and Liu, Lirong and Leach, Matthew
MDPI Sustainability 2024
https://www.mdpi.com/2071-1050/16/11/4710

This is designed to run in EnergyPlus V24.2 or newer.

! Some features of 10.3390/su16114710 bungalow, Salford EH1 weather.
! NOTE: Salford location and design day lines copied in from EH1 model.
!
! hart-davis2024zone bungalow parameters:
!     IWL (Internal Wall Length) = 4m, thus whole external wall length 8m.
!     IWH (Internal Wall Height) = 2.3m
!     EWRU (Effective Wall and Roof U-value): 0.61 W/m2K
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

See some basics of the IDF file:
    https://bigladdersoftware.com/epx/docs/9-2/input-output-reference/group-simulation-parameters.html
    
When running design day, "Annual and Peak Values - Other" maximum seems useful.


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