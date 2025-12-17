#!/bin/sh

# Extract from CSVs for all AAAA/AABB/ABAB and WC/LC combinations.

for control in LC WC;
  do
      for pattern in AAAA AABB ABAB;
          do
              sourceCSV="out-dd-${pattern}-${control}/eplusout.csv"
              sh extract-from-DD-csv.sh "$sourceCSV"
          done
  done
