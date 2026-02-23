#!/bin/sh

printf "Running AAAA model"
energyplus-24.2.0 -r -d out-dd-AAAA -D bungalow-2-heatpump-AAAA.idf

printf "Running ABAB model"
energyplus-24.2.0 -r -d out-dd-ABAB -D bungalow-2-heatpump-ABAB.idf

printf "Running AABB model"
energyplus-24.2.0 -r -d out-dd-AABB -D bungalow-2-heatpump-AABB.idf
