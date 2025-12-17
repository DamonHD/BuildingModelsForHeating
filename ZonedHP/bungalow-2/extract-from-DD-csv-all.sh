#!/bin/sh

# Extract from CSVs for all AAAA/AABB/ABAB and WC/LC combinations.

echo "simulation_name,z1_C,z2_C,z3_C,z4_C,heat_demand_W,electricity_demand_W"
for control in LC WC;
  do
      for pattern in AAAA AABB ABAB;
          do
              sourceCSV="out-dd-${pattern}-${control}/eplusout.csv"
              sh extract-from-DD-csv.sh "$sourceCSV"
          done
  done
