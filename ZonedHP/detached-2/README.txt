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
 
 
 
 
 
 

NOTES / Changes
===============

DHD20260409T10:38Z runs as a clone of bungalow-2.
DHD20260409: raised roof 2.3m, exterior walls for 1st floor,  ...