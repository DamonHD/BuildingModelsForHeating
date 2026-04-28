#!/bin/sh

# Extract representative info from steady-state design-day heat-pump .csv output.
#
# Usage:
#     $0 DD-run-dir/eplusout.csv
#
# eg:
#     sh detached-extract-from-DD-csv.sh out-dd-AAAA-LC/eplusout.csv
#     out-dd-AAAA-LC,21.0,21.0,21.0,21.0,1778,742


# Extracts from final (24:00) row named input .csv file.
# Writes to stdout short csv line of which first cell is directory of filename.
# This output contains key parameter values: zone temps, heat demand, H4 demand.
# The output values are rounded to a sensible precision.
# Input filename must not contain commas, spaces, quotes or tricky metachars.
# In case of error returns no output on stdout, or line starting "ERROR: ".

INPUT="$1"

if [ ! -s "$INPUT" ]; then exit 1; fi

exec awk -F, < "$INPUT" -v INPUTDIR="$(dirname "$INPUT")" '

    BEGIN {
    # Find the correct index/field for each output value required by name.
    z1namePref="Z1:Zone Operative Temperature [C](Hourly)"
    z2namePref="Z2:Zone Operative Temperature [C](Hourly)"
    z3namePref="Z3:Zone Operative Temperature [C](Hourly)"
    z4namePref="Z4:Zone Operative Temperature [C](Hourly)"
    z5namePref="Z5:Zone Operative Temperature [C](Hourly)"
    z6namePref="Z6:Zone Operative Temperature [C](Hourly)"
    z7namePref="Z7:Zone Operative Temperature [C](Hourly)"
    z8namePref="Z8:Zone Operative Temperature [C](Hourly)"
    z1name="Z1:Zone Air Temperature [C](Hourly)"
    z2name="Z2:Zone Air Temperature [C](Hourly)"
    z3name="Z3:Zone Air Temperature [C](Hourly)"
    z4name="Z4:Zone Air Temperature [C](Hourly)"
    z5name="Z5:Zone Air Temperature [C](Hourly)"
    z6name="Z6:Zone Air Temperature [C](Hourly)"
    z7name="Z7:Zone Air Temperature [C](Hourly)"
    z8name="Z8:Zone Air Temperature [C](Hourly)"
    pumpname="SUPPLY PUMP:Pump Electricity Rate [W](Hourly)"
    heatdemandname="Baseboard Total Heating Rate All Zones:PythonPlugin:OutputVariable [W](Hourly) "
    hpname="HEAT PUMP:Heat Pump Electricity Rate [W](Hourly)"
    flowTname="HEAT PUMP:Heat Pump Load Side Outlet Temperature [C](Hourly)"
    returnTname="HEAT PUMP:Heat Pump Load Side Inlet Temperature [C](Hourly)"
    }
 
    # Extract the index (field number) for the given E+ variable.
    # A preferred name is given first, then an alternate/fallback.
    # Exit with an error if not found.
    function getIndex(varNamePref, varNameAlt) {
        for(i = 2; i <= NF; ++i) {
            if($i == varNamePref) { return(i); }
            }
        #print "ERROR: did not find: "varNamePref;
        for(i = 2; i <= NF; ++i) {
            if($i == varNameAlt) { return(i); }
            }
        print "ERROR: did not find: "varNamePref" or "varNameAlt;
        exit 1
        }
 
    NR==1 {
        # Capture header line and field indices.
        if("Date/Time" != $1) { print "ERROR: bad header"; exit 1; }
        z1i = getIndex(z1namePref,z1name);
        z2i = getIndex(z2namePref,z2name);
        z3i = getIndex(z3namePref,z3name);
        z4i = getIndex(z4namePref,z4name);
        z5i = getIndex(z5namePref,z5name);
        z6i = getIndex(z6namePref,z6name);
        z7i = getIndex(z7namePref,z7name);
        z8i = getIndex(z8namePref,z8name);
        pumpi = getIndex(pumpname,"");
        heatdemandi = getIndex(heatdemandname,"");
        hpi = getIndex(hpname,"");
        flowTi = getIndex(flowTname,"");
        returnTi = getIndex(returnTname,"");
        }

    $1 ~ /24:00:00$/ {
        # Extract values from final hour of the simulation results.
        printf("%s,", INPUTDIR);
        z1=$z1i; z2=$z2i; z3=$z3i; z4=$z4i;
        z5=$z5i; z6=$z6i; z7=$z7i; z8=$z8i;
        heatdemand=$heatdemandi;
        pump=$pumpi
        hp=$hpi
        h4=pump+hp
        flowT=$flowTi
        returnT=$returnTi
        printf("%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%0.f,%.0f,%.1f,%.1f\n", z1,z2,z3,z4,z5,z6,z7,z8, heatdemand, h4, flowT, returnT);
        exit;
    }
    '

# Should not get here.
exit 1
