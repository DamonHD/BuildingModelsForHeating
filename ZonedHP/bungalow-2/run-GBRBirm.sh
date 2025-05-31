#!/bin/sh
# Run bungalow-2.idf for a whole year with UK representative weather.

if [ "" = "${WEATHERDIR}" ]; then
    echo "ERROR: please set WEATHERDIR" 1>&2
    exit 1
fi

exec /Applications/EnergyPlus-24-2-0/energyplus -d out-GBRBirm -w ${WEATHERDIR}/GBR_Birmingham.035340_IWEC.epw bungalow-2.idf
