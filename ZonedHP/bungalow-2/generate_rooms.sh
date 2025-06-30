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

# Controls the radiator sizing using the
# ZoneHVAC:Baseboard:Convective:Water::UA-factor parameter.
#
# This value is chosen so that the not-setback case is correctly sized,
# but the setback cases are undersized, causing a ~1K drop in room temperature
# in the A rooms.
RAD_SIZING_AAAA=13.90
# This value is chosen so that the radiators are oversized in all rooms/cases.
# The A rooms will maintain their temperature in all cases.
RAD_SIZING_OVERSIZED=20.00

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
    -e "s/::RAD_UA_FACTOR::/${RAD_SIZING_AAAA}/g" \
    $TEMPLATE > bungalow-2-heatpump-AAAA.idf

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
    -e "s/::RAD_UA_FACTOR::/${RAD_SIZING_AAAA}/g" \
    $TEMPLATE > bungalow-2-heatpump-ABAB.idf

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
    -e "s/::RAD_UA_FACTOR::/${RAD_SIZING_AAAA}/g" \
    $TEMPLATE > bungalow-2-heatpump-AABB.idf
