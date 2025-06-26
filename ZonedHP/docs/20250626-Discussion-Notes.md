# 20250626 Discussion Notes

DHD20250626

DHD has not resolved heat-demand issues with bungalow-2 yet, but DE should maybe start integrating the heat pump in to a variant of that, and capture a version that reproduces the bad setback effect and the mitigations per DHD’s paper.  This implies AAAA ABAB and AABB with both rads only exactly big enough for AAAA and thus vulnerable to bad setback effect **and** AAAA ABAB and AABB with rads sized to make the effect go away.  And a note of about how oversized that requires.  All rads sized the same.  

## Note on above

To support and link to conclusions from DHD’s paper:

1. Have bungalow-2 model with weather comp (flow temp set by external temperature) drive AAAA, ABAB, AABB variants and show \~15% heat demand and electricity reduction in the non-AAAA modes, in return for a 1K to 2K temperature sag in A rooms.  (Suggest max flow rate 24l/m.)  
2. Have bungalow-2 model per Heat Geek bad-setback case, with rads sized just large enough for AAAA, flow temp dynamically adjusted to regulate A room temp, and CoP curve (and flow temp bounds) set to match DHD’s paper.  Electricity demand should go up even as heat demand goes down in ABAB and AABB cases.  The ^1.2 factor in heat emission from radiator mean temperature to room temperature may be important.  (Suggest max flow rate 24l/m.)

### Other points

1. All rads receive same flow temperature water: flow rate restriction by TRV determines reduced heat output.  
2. Is the heat pump flow rate constant in each case above?  DHD’s system dynamically varies flow between 8l/min and 24l/min based it seems on delta-T flow to return; if the model has to do something similar, that is OK, but mass flow should be capped\!  Real heat pumps have minimum flow requirements.  In DHD’s system an ABV (Automatic Bypass Value, pressure drive) ensures minimum flow.  Real heat pump system require a minimum volume, at least ASHPs do.  In DHD’s system this is met by the volumiser on the return to the external unit.  Fix flow rate or vary it within bounds, maybe maintaining a fairly constant pressure.  I suspect that installers who don’t like TRVs will like constant flow circulation pumps.  
3. Suggestion: in the HG case, constant flow, aiming for flow/return delta-T of 5K, no TRVs in A rooms, so guaranteed flow, but don’t worry explicitly about a minimum.  
4. Suggestion: in the non-HG case, try whatever you have in the HG case by preference for consistency, else variable flow to meet a flow/return delta-T of 5K.  
5. EH1 HTC is \~170W/K.  For bungalow 1 or 2 its is 2kW/(21 \- \-3).  From that, max mass flow rate can be constrained.  
6. Flow temp should be no higher than 55C (per English Building regs and DHD’s home system).  But use the values from DHD’s paper.  Use the CoP curve from the paper.  
7. Suggest lower bound on flow temperature is 25C per DHD’s home system.  
8. DHD’s weather curve is 25C flow at 15C external, 55C flow at \-7C external.  Full horrors: [https://www.earth.org.uk/heat-pump-16WW-control.html](https://www.earth.org.uk/heat-pump-16WW-control.html)  
9. DHD’s flow rate bounds nominally 6l/min to 24l/min.  Usually runs at 8l/min for spce heat, 24l/min for DHW.  
10. DHD experience suggests that \> 8l/min makes for noisy radiator valves.

### All b2 cases to be modelled at design day steady external temps

In each case note (a) electricity demand (b) room temps (c) heat demand.

* HG mode (load comp w/ variable flow temp to maintain A rooms at 21C, minimal rads): AAAA, ABAB, AABB  
* Non-HG mode (weather comp w/ external temp setting flow temp, to maintain A rooms at 21C in AAAA mode at design day, oversized rads): AAAA, ABAB, AABB

