Continuation of bungalow-1, 4 zoned AAAA or AABB or ABAB, from DOI 10.3390/su16114710
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
!     External wall and roof surface: (4x18.4m2 + 64m2) 137.6m2
!     Floor non-conducting
!     IDU (Internal Door U-value): 8 W/m2K
!     IWU (Internal Wall U-value): 2 W/m2K
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
! Computed effective external wall and roof U value (EWRU): 0.61 W/m2K

! Acknowledgements:
!
! DERIVED FROM EH1 fragments with permission, and EnergyPlus shipped files:
!     Minimal.idf Example1A.idf 1ZoneUncontrolled.idf
!
! See https://energyplus.readthedocs.io/en/latest/acknowledgments/acknowledgments.html
! NOTICE: The U.S. Government is granted for itself and others acting on its behalf a paid-up, nonexclusive, irrevocable, worldwide license in this data to reproduce, prepare derivative works, and perform publicly and display publicly. Beginning five (5) years after permission to assert copyright is granted, subject to two possible five year renewals, the U.S. Government is granted for itself and others acting on its behalf a paid-up, non-exclusive, irrevocable worldwide license in this data to reproduce, prepare derivative works, distribute copies to the public, perform publicly and display publicly, and to permit others to do so.

Note that GB weather files are available from:
    https://energyplus.net/weather-region/europe_wmo_region_6/GBR
These include Aberdeen, Birmingham, Jersey, London Gatwick.
The licence does not apparently allow redistribution:
    https://energyplus.net/assets/nrel_custom/weather/ashrae_license_agreement.txt

Note that Construction CTF shows U-value (ThermalConductance) for each construction.

Some basics of the IDF file:
    https://bigladdersoftware.com/epx/docs/9-2/input-output-reference/group-simulation-parameters.html
    

NOTES
=====

DHD20250413: now 28.35GJ (7876kWh, 900W) annual for Birmingham weather annual simulation.  (Manchester EGCC from paper 875W.)
DHD20250531: ... bungalow-1 nominally cloned to bungalow-2.
DHD20250602: ... conversion to 4-zone continues ...