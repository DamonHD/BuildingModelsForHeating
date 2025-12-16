#!/bin/sh

# Extract representative info from steady-state design-day heat-pump .csv output.
#
# Usage:
#     $0 DD-run-dir/eplusout.csv
#
# eg:
#     sh extract-from-DD-csv.sh out-dd-AAAA-LC/eplusout.csv


# Extracts from final (24:00) row named input .csv file.
# Writes to stdout short csv line of which first cell is directory of filename.
# Input filename must not contain commas, spaces, quotes or tricky metachars.
# In case of error returns no output on stdout.

INPUT="$1"

if [ ! -s "$INPUT" ]; then exit 1; fi
