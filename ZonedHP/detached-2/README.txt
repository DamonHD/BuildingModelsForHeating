Detached house, heat pump, 8 zoned AAAA or AABB or ABAB, from DOI 10.3390/su16114710
To Zone or Not to Zone When Upgrading a Wet Heating System from Gas to Heat Pump for Maximum Climate Impact: A UK View
Hart-Davis, Damon and Liu, Lirong and Leach, Matthew
MDPI Sustainability 2024
https://www.mdpi.com/2071-1050/16/11/4710

Called 'detached-2' to match 'bungalow-2'.

Floor plan is same as bungalow-2, building has two levels.

Partial run script (with tests):
% sh detached-2-generate_rooms.sh && \
  sh detached-2-runall-dd.sh && \
  sh detached-2-extract-from-DD-csv-all.sh && \
  python3 ./detached-2-test.py
  

 
 NEXT: clone interior walls for 1st floor, insert interior floor between gnd/1st.
 TODO: break out "445, !- Heating Design Capacity {W}" as RAD_XXX external variable.
 TODO: break out total flow and capacity of system to external variables?


DHD20260515: before introducing/changing RAD2_UA_FACTOR:
    out-dd-AAAA-LC,21.0,21.0,21.0,21.0,19.3,19.3,19.3,19.3,1230,835,37.9,32.9
    out-dd-AABB-LC,21.0,21.0,18.0,18.0,19.3,19.3,18.0,18.0,1056,818,38.5,33.8
	out-dd-ABAB-LC,21.0,18.0,18.0,21.0,18.0,19.3,19.3,18.0,1083,873,40.9,36.1
	out-dd-AAAA-WC,21.0,21.0,21.0,21.0,21.0,21.0,21.0,21.0,1014,1076,46.0,40.9
	out-dd-AABB-WC,21.0,21.0,18.0,18.0,21.0,21.0,18.0,18.0,951,1016,46.0,41.2
	out-dd-ABAB-WC,21.0,18.0,18.0,21.0,18.0,20.5,20.5,18.0,1031,1010,46.0,41.2
Room heat loss from upstairs wrt downstairs
    = (roof area + ext wall area) / ext wall area
    = (16m^2 + 18.4m^2) / 18.4m^2
    = ~1.87
Thus updated IDF generator to:
	# DHD20260515: shrunk by ~1.87x to reflect reduced heat loss downstairs.
	RAD_UA_FACTOR=16.31
	# DHD20260515: second (upstairs) radiator size; same as for bungalow-2.
	RAD2_UA_FACTOR=30.50
Results in:
	out-dd-AAAA-LC,21.0,21.0,21.0,21.0,21.0,21.0,21.0,21.0,1015,1001,43.1,37.9
	out-dd-AABB-LC,21.0,21.0,18.0,18.0,21.0,21.0,18.0,18.0,951,1004,45.5,40.7
	out-dd-ABAB-LC,20.9,18.0,18.0,20.9,18.0,21.0,21.0,18.0,1003,1148,51.5,46.7
	out-dd-AAAA-WC,21.0,21.0,21.0,21.0,21.0,21.0,21.0,21.0,1014,1076,46.0,40.9
	out-dd-AABB-WC,21.0,21.0,18.0,18.0,21.0,21.0,18.0,18.0,951,1016,46.0,41.2
	out-dd-ABAB-WC,20.1,18.0,18.0,20.1,18.0,20.4,20.4,18.0,937,1001,46.0,41.3



pytest detached-2-test.py
https://docs.pytest.org/en/stable/how-to/output.html
https://docs.pytest.org/en/stable/how-to/capture-stdout-stderr.html
 
 
 

NOTES / Changes
===============

DHD20260409T10:38Z now runs as a clone of bungalow-2.
DHD20260409: raised roof 2.3m to make space for 1st floor (F1)
DHD20260409: created exterior walls for 1st floor (against new zones Z5 to Z8)
DHD20260409: created new zones Z5 to Z8 and associated radiators etc
DHD20260420: adding IF MEAN internal floor material to match IW MEAN internal wall thermally, per paper
DHD20260428: internal floors inserted
DHD20260515: fixed plugin and tests for 8 zones
DHD20260515: checked that Heating Design Capacity {W} number (was 445, now 9999) not magic (may in fact be ignored)
