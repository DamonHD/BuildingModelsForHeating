#!/bin/sh
# Run IDF for winter design day.

#if [ "" = "${WEATHERDIR}" ]; then
#    echo "ERROR: please set WEATHERDIR" 1>&2
#    exit 1
#fi

exec /Applications/EnergyPlus-9-4-0/energyplus -d out-7mod-dd -D 7mod.idf
