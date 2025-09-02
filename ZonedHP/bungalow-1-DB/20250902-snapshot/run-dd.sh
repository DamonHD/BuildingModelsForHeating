#!/bin/sh
# Run bungalow-1.idf for winter design day.

#if [ "" = "${WEATHERDIR}" ]; then
#    echo "ERROR: please set WEATHERDIR" 1>&2
#    exit 1
#fi

exec /Applications/EnergyPlus-9-4-0/energyplus -d out-dd -D 1.idf
