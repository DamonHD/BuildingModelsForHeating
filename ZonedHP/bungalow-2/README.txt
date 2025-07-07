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
!     IDU (Internal Door U-value) = 8W/m2K
!     IDA (Internal Door Area) = 2m2 (with one full door per wall)
!     IWU (Internal Wall U-value) = 2W/m2K (~plasterboard on studs)     
!         Effective overall internal wall (7.2m2) and door (2m2) U-value ~ 3.30W/m2K.
!     EWRU (Effective Wall and Roof U-value): 0.61 W/m2K
!     External wall and roof surface: (4x18.4m2 + 64m2) 137.6m2
!     Floor non-conducting
!     IDU (Internal Door U-value): 8 W/m2K
!     IWU (Internal Wall U-value): 2 W/m2K
!     Interior and exterior temperatures at design conditions: 21C / -3C
!     Expected heat demand at design conditions: 2000W
!     Whole house HTC ~ 83.3W/K
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


! Zone Description Details, floor plan:
!
!          (0,8,0)        (4,8,0)       (8,8,0)
!              ______NE____________NW______
!             |              |             |
!             |              |             |
!             |              |             |
!           EN|      Z3      |     Z4      |WN
!             |              |             |
!             |              | (4,4,0)     |
!     (0,4,0) |--------------+-------------| (8,4,0)
!             |              |             |
!             |              |             |
!           ES|      Z1      |     Z2      |WS
!             |              |             |
!             |              |             |
!             |______________|_____________|
!                    SE            SW
!          (0,0,0)        (4,0,0)       (8,0,0)
!
! NW = Z4
!    4,4,0,  !- X,Y,Z ==> Vertex 1 {m}
!    4,8,0,  !- X,Y,Z ==> Vertex 2 {m}
!    8,8,0,  !- X,Y,Z ==> Vertex 3 {m}
!    8,4,0;  !- X,Y,Z ==> Vertex 4 {m}
! NE = Z3
!    0,4,0,  !- X,Y,Z ==> Vertex 1 {m}
!    0,8,0,  !- X,Y,Z ==> Vertex 2 {m}
!    4,8,0,  !- X,Y,Z ==> Vertex 3 {m}
!    4,4,0;  !- X,Y,Z ==> Vertex 4 {m}
! SE = Z1
!    0,0,0,  !- X,Y,Z ==> Vertex 1 {m}
!    0,4,0,  !- X,Y,Z ==> Vertex 2 {m}
!    4,4,0,  !- X,Y,Z ==> Vertex 3 {m}
!    4,0,0;  !- X,Y,Z ==> Vertex 4 {m}
! SW = Z2
!    4,0,0,  !- X,Y,Z ==> Vertex 1 {m}
!    4,4,0,  !- X,Y,Z ==> Vertex 2 {m}
!    8,4,0,  !- X,Y,Z ==> Vertex 3 {m}
!    8,0,0;  !- X,Y,Z ==> Vertex 4 {m}

USAGE
=====

Basic command:
	$ ./generate_rooms.sh && ./runall-dd.sh

Generating .idf files
---------------------

In order to support multiple scenarios, an .idf file is generated per scenario using
the `generate_rooms.sh` script.
- Input file: bungalow-2-heatpump.template
- Output files: bungalow-2-{scenario-name}.idf

Running the Simulations
-----------------------

All scenarios can be run at once using the `runall-dd.sh` script.
An output folder is generated per scenario.
- Input files: bungalow-2-{scenario-name}.idf
- Output folders: out-dd-{scenario-name}/

Running Tests
-------------

If python is installed (tested on v3.13.3), outputs can by sanity checked
by running test_bungalow-2.py. Note that tests are run against the output
of runall-dd.sh, and so `$ ./generate_rooms.sh && ./runall-dd.sh`
should be run before running the tests.

If pytest is installed as an optional dependency,
it can be used as a test harness using the following command in this folder:
	bungalow-2$ pytest

Otherwise, tests can be run as a normal python script:
	bungalow-2$ python test_bungalow-2.py

NOTES
=====

DHD20250413: 'operative' (@0.5) thermostat raises ZONE ONE PURCHASED AIR,Zone Ideal Loads Zone Total Heating Rate [W] to 2025W (cf 3825W at 0.89).
DHD20250413: now 28.35GJ (7876kWh, 900W) annual for Birmingham weather annual simulation.  (Manchester EGCC from paper 875W.)
DHD20250531: ... bungalow-1 nominally cloned to bungalow-2.
DHD20250602: ... conversion to 4-zone continues ...
DHD20250604: walls, roof, floor split to allow creation of Z1, Z2, Z3, Z4; 2025W heat loss as was.
 DE20250623: coordinate errors fixed for bungalow-2; heat demand before and after 1777W.
DHD20250624: bungalow-2-dezoned.idf heat load back to 2025W.
DHD20250624: asked question: https://unmethours.com/question/102055/adding-internal-partitions-reduces-heatflow-to-outside-why/
 DE20250625: Implemented setback scenarios
 DE20250626: Fixed bungalow-2 flow rates and radiator sizing, disabled Thermostat:OperativeTemparature.
DHD20250627: partition effective U-value (w/film) now 3.30W/m2K to match paper's implied values.
 DE20250628: Fixed simulation issues.
 DE20250630: Added python sense check
 DE20250630: Fixed simulation issues (again)
 DE20250702: Modified heatpump to reflect DHD model from paper
 DE20250707: Implemented load and weather compensation plugins
