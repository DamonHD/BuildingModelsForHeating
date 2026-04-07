#!/bin/sh

# WIP!

# The zone layout of the model GROUND FLOOR:
# +---------+
# | Z3 | Z4 |
# |----+----|
# | Z1 | Z2 |
# +---------+
#
# The floor above (zone is that of the room below + 4):
# +---------+
# | Z7 | Z8 |
# |----+----|
# | Z5 | Z6 |
# +---------+
#
# 'A' zones are set to 21 C
# 'B' zones are set to 18 C

TEMPLATE='detached-2-heatpump.template'

# Chooses between the load and weather compensated control schemes.
LC_CONTROL_SCHEME=LoadCompHeatPumpController
WC_CONTROL_SCHEME=WeatherCompHeatPumpController

# Controls the radiator sizing using the
# ZoneHVAC:Baseboard:Convective:Water::UA-factor parameter.
#
# This value is chosen so that the not-setback case is correctly sized,
# but the setback cases are undersized, causing a ~1K drop in room temperature
# in the A rooms.
# DHD20260407: bungalow-2 values RAD_UA_FACTOR=30.5 RAD_FLOW_MAX=0.03e-3
RAD_UA_FACTOR=30.50
RAD_FLOW_MAX=0.03e-3

# Design day outside air temperature
#
# Sets both the wet and dry bulbs to this value.
# NOTE: Bad setback effect on LC models stops above 2 C
# Usual target value: DD_OUTSIDE_TEMP=-3.0
# For WC curve calibration: DD_OUTSIDE_TEMP=15.0
# For easy calculation of the intercept: DD_OUTSIDE_TEMP=0.0
DD_OUTSIDE_TEMP=-3.0

# Generate the AAAA, ABAB and AABB cases from the given parameters
# $1: Heat pump control scheme, one of LC_CONTROL_SCHEME and WC_CONTROL_SCHEME
# $2: Radiator UA Factor (sizing).
# $3: Maximum radiator flow rate.
# $4: Design day outside temperature
generate_case () {
# AAAA
# +-------+    +-------+
# | A | A | up | A | A |
# |---+---| -> +---+---+
# | A | A |    | A | A |
# +-------+    +-------+
sed -e "s/::Z1_SETPOINT_CONTROL::/Not Setback Setpoint Control/g" \
    -e "s/::Z2_SETPOINT_CONTROL::/Not Setback Setpoint Control/g" \
    -e "s/::Z3_SETPOINT_CONTROL::/Not Setback Setpoint Control/g" \
    -e "s/::Z4_SETPOINT_CONTROL::/Not Setback Setpoint Control/g" \
    -e "s/::Z5_SETPOINT_CONTROL::/Not Setback Setpoint Control/g" \
    -e "s/::Z6_SETPOINT_CONTROL::/Not Setback Setpoint Control/g" \
    -e "s/::Z7_SETPOINT_CONTROL::/Not Setback Setpoint Control/g" \
    -e "s/::Z8_SETPOINT_CONTROL::/Not Setback Setpoint Control/g" \
    -e "s/::HP_CONTROL_SCHEME::/$1/g" \
    -e "s/::RAD_UA_FACTOR::/$2/g" \
    -e "s/::RAD_FLOW_MAX::/$3/g" \
    -e "s/::DD_OUTSIDE_TEMP::/$4/g" \
    $TEMPLATE > detached-2-heatpump-AAAA-$1.idf

# ABAB
# +-------+    +-------+
# | B | A | up | A | B |
# |---+---| -> +---+---+
# | A | B |    | B | A |
# +-------+    +-------+
sed -e "s/::Z1_SETPOINT_CONTROL::/Not Setback Setpoint Control/g" \
    -e "s/::Z2_SETPOINT_CONTROL::/Setback Setpoint Control/g" \
    -e "s/::Z3_SETPOINT_CONTROL::/Setback Setpoint Control/g" \
    -e "s/::Z4_SETPOINT_CONTROL::/Not Setback Setpoint Control/g" \
    -e "s/::Z5_SETPOINT_CONTROL::/Setback Setpoint Control/g" \
    -e "s/::Z6_SETPOINT_CONTROL::/Not Setback Setpoint Control/g" \
    -e "s/::Z7_SETPOINT_CONTROL::/Not Setback Setpoint Control/g" \
    -e "s/::Z8_SETPOINT_CONTROL::/Setback Setpoint Control/g" \
    -e "s/::HP_CONTROL_SCHEME::/$1/g" \
    -e "s/::RAD_UA_FACTOR::/$2/g" \
    -e "s/::RAD_FLOW_MAX::/$3/g" \
    -e "s/::DD_OUTSIDE_TEMP::/$4/g" \
    $TEMPLATE > detached-2-heatpump-ABAB-$1.idf

# AABB
# +-------+    +-------+
# | B | B | up | B | B |
# |---+---| -> +---+---+
# | A | A |    | A | A |
# +-------+    +-------+
sed -e "s/::Z1_SETPOINT_CONTROL::/Not Setback Setpoint Control/g" \
    -e "s/::Z2_SETPOINT_CONTROL::/Not Setback Setpoint Control/g" \
    -e "s/::Z3_SETPOINT_CONTROL::/Setback Setpoint Control/g" \
    -e "s/::Z4_SETPOINT_CONTROL::/Setback Setpoint Control/g" \
    -e "s/::Z5_SETPOINT_CONTROL::/Not Setback Setpoint Control/g" \
    -e "s/::Z6_SETPOINT_CONTROL::/Not Setback Setpoint Control/g" \
    -e "s/::Z7_SETPOINT_CONTROL::/Setback Setpoint Control/g" \
    -e "s/::Z8_SETPOINT_CONTROL::/Setback Setpoint Control/g" \
    -e "s/::HP_CONTROL_SCHEME::/$1/g" \
    -e "s/::RAD_UA_FACTOR::/$2/g" \
    -e "s/::RAD_FLOW_MAX::/$3/g" \
    -e "s/::DD_OUTSIDE_TEMP::/$4/g" \
    $TEMPLATE > detached-2-heatpump-AABB-$1.idf
}

generate_case $LC_CONTROL_SCHEME $RAD_UA_FACTOR $RAD_FLOW_MAX $DD_OUTSIDE_TEMP
generate_case $WC_CONTROL_SCHEME $RAD_UA_FACTOR $RAD_FLOW_MAX $DD_OUTSIDE_TEMP

