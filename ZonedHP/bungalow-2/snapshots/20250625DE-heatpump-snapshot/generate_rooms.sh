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
    $TEMPLATE > bungalow-2-heatpump-AABB.idf
