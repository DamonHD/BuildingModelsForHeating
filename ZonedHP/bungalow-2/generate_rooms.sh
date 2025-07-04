#!/bin/sh

# The zone layout of the model:
# +---------+
# | Z3 | Z4 |
# |----+----|
# | Z1 | Z2 |
# +---------+
#
# 'A' zones are set to 21 C
# 'B' zones are set to 18 C

TEMPLATE='bungalow-2-heatpump.template'

# Chooses between the load and weather compensated control schemes.
LC_CONTROL_SCHEME=LoadCompHeatPumpController
WC_CONTROL_SCHEME=WeatherCompHeatPumpController

# Controls the radiator sizing using the
# ZoneHVAC:Baseboard:Convective:Water::UA-factor parameter.
#
# This value is chosen so that the not-setback case is correctly sized,
# but the setback cases are undersized, causing a ~1K drop in room temperature
# in the A rooms.
RAD_UA_FACTOR=20.00
RAD_FLOW_MAX=0.03e-3

# This value is chosen so that the radiators are oversized in all rooms/cases.
# The A rooms will maintain their temperature in all cases.
RAD_SIZING_OVERSIZED=20.00

generate_case () {
# AAAA
# +-------+
# | A | A |
# |---+---|
# | A | A |
# +-------+
sed -e "s/::Z1_SETPOINT_CONTROL::/Not Setback Setpoint Control/g" \
    -e "s/::Z2_SETPOINT_CONTROL::/Not Setback Setpoint Control/g" \
    -e "s/::Z3_SETPOINT_CONTROL::/Not Setback Setpoint Control/g" \
    -e "s/::Z4_SETPOINT_CONTROL::/Not Setback Setpoint Control/g" \
    -e "s/::RAD_UA_FACTOR::/$2/g" \
    -e "s/::RAD_FLOW_MAX::/$3/g" \
    -e "s/::HP_CONTROL_SCHEME::/$1/g" \
    $TEMPLATE > bungalow-2-heatpump-AAAA-$1.idf

# ABAB
# +-------+
# | B | A |
# |---+---|
# | A | B |
# +-------+
sed -e "s/::Z1_SETPOINT_CONTROL::/Not Setback Setpoint Control/g" \
    -e "s/::Z2_SETPOINT_CONTROL::/Setback Setpoint Control/g" \
    -e "s/::Z3_SETPOINT_CONTROL::/Setback Setpoint Control/g" \
    -e "s/::Z4_SETPOINT_CONTROL::/Not Setback Setpoint Control/g" \
    -e "s/::RAD_UA_FACTOR::/$2/g" \
    -e "s/::RAD_FLOW_MAX::/$3/g" \
    -e "s/::HP_CONTROL_SCHEME::/$1/g" \
    $TEMPLATE > bungalow-2-heatpump-ABAB-$1.idf

# AABB
# +-------+
# | B | B |
# |---+---|
# | A | A |
# +-------+
sed -e "s/::Z1_SETPOINT_CONTROL::/Not Setback Setpoint Control/g" \
    -e "s/::Z2_SETPOINT_CONTROL::/Not Setback Setpoint Control/g" \
    -e "s/::Z3_SETPOINT_CONTROL::/Setback Setpoint Control/g" \
    -e "s/::Z4_SETPOINT_CONTROL::/Setback Setpoint Control/g" \
    -e "s/::RAD_UA_FACTOR::/$2/g" \
    -e "s/::RAD_FLOW_MAX::/$3/g" \
    -e "s/::HP_CONTROL_SCHEME::/$1/g" \
    $TEMPLATE > bungalow-2-heatpump-AABB-$1.idf
}

generate_case $LC_CONTROL_SCHEME $RAD_UA_FACTOR $RAD_FLOW_MAX
generate_case $WC_CONTROL_SCHEME $RAD_UA_FACTOR $RAD_FLOW_MAX

