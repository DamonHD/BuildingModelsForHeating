#!/bin/sh
# Run bungalow-2-dezoned.idf for winter design day.

#if [ "" = "${WEATHERDIR}" ]; then
#    echo "ERROR: please set WEATHERDIR" 1>&2
#    exit 1
#fi

exec /Applications/EnergyPlus-24-2-0/energyplus -d out-dezoned-dd -D bungalow-2-dezoned.idf
