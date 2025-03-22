#!/bin/sh
# bungalow-1.idf

if [ "" = "${WEATHERDIR}" ]; then
    echo "ERROR: please set WEATHERDIR" 1>&2
    exit 1
fi

exec /Applications/EnergyPlus-24-2-0/energyplus -d out-2-GBRBirm -w ${WEATHERDIR}/GBR_Birmingham.035340_IWEC.epw bungalow-1.idf
