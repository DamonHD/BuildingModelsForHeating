#!/bin/sh

# Extract representative info from steady-state design-day heat-pump .csv output.
#
# Usage:
#     $0 DD-run-dir/eplusout.csv
#
# eg:
#     sh extract-from-DD-csv.sh out-dd-AAAA-LC/eplusout.csv
#     out-dd-AAAA-LC,21.0,21.0,21.0,21.0,1778,742


# Extracts from final (24:00) row named input .csv file.
# Writes to stdout short csv line of which first cell is directory of filename.
# This output contains key parameter values: zone temps, heat demand, H4 demand.
# The output values are rounded to a sensible precision.
# Input filename must not contain commas, spaces, quotes or tricky metachars.
# In case of error returns no output on stdout.

INPUT="$1"

if [ ! -s "$INPUT" ]; then exit 1; fi

exec awk -F, < "$INPUT" -v INPUTDIR="$(dirname "$INPUT")" '
    $1 ~ /24:00:00$/ {
        printf("%s,", INPUTDIR);
        z1=$3; z2=$4; z3=$5; z4=$6;
        #printf("%.1f,", z1);#DEBUG
        heatdemand=$22;
        pump=$19
        hp=$18
        h4=pump+hp
        #printf("%.0f,%0.f,%0.f,%.0f\n", pump, hp, h4, heatdemand);#DEBUG
        printf("%.1f,%.1f,%.1f,%.1f,%0.f,%.0f\n", z1,z2,z3,z4, heatdemand, h4);
        exit;
    }
    '

# Should not get here.
exit 1

# Expected input final line something like:
# 01/15  24:00:00,-3.0,21.00053090490247,21.00053090490247,21.00053090490247,21.00053090490247,49.51786601458085,444.4342197298223,0.02938078125,444.4342197298223,0.02938078125,444.4342197298223,0.02938078125,444.4342197298223,0.02938078125,1775.40800725105,46.250507009285904,739.661335955638,1.9701930374573164,1.9701930374573164,0.12998674,1777.7368789192892

# Expected input header line something like:
# Date/Time,Environment:Site Outdoor Air Drybulb Temperature [C](Hourly),Z1:Zone Air Temperature [C](Hourly),Z2:Zone Air Temperature [C](Hourly),Z3:Zone Air Temperature [C](Hourly),Z4:Zone Air Temperature [C](Hourly),HOT WATER LOOP:Plant Supply Side Outlet Temperature [C](Hourly),Z1 RADIATOR:Baseboard Total Heating Rate [W](Hourly),Z1 RADIATOR:Baseboard Hot Water Mass Flow Rate [kg/s](Hourly),Z2 RADIATOR:Baseboard Total Heating Rate [W](Hourly),Z2 RADIATOR:Baseboard Hot Water Mass Flow Rate [kg/s](Hourly),Z3 RADIATOR:Baseboard Total Heating Rate [W](Hourly),Z3 RADIATOR:Baseboard Hot Water Mass Flow Rate [kg/s](Hourly),Z4 RADIATOR:Baseboard Total Heating Rate [W](Hourly),Z4 RADIATOR:Baseboard Hot Water Mass Flow Rate [kg/s](Hourly),HEAT PUMP:Heat Pump Load Side Heat Transfer Rate [W](Hourly),HEAT PUMP:Heat Pump Load Side Inlet Temperature [C](Hourly),HEAT PUMP:Heat Pump Electricity Rate [W](Hourly),SUPPLY PUMP:Pump Electricity Rate [W](Hourly),SUPPLY PUMP:Pump Fluid Heat Gain Rate [W](Hourly),SUPPLY PUMP:Pump Mass Flow Rate [kg/s](Hourly),Baseboard Total Heating Rate All Zones:PythonPlugin:OutputVariable [W](Hourly) 
