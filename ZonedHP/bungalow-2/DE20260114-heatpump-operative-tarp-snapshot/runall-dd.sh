#!/bin/sh

printf "Running AAAA model with load compensation\n"
energyplus-24.2.0 -r -d out-dd-AAAA-LC -D bungalow-2-heatpump-AAAA-LoadCompHeatPumpController.idf

printf "Running ABAB model with load compensation\n"
energyplus-24.2.0 -r -d out-dd-ABAB-LC -D bungalow-2-heatpump-ABAB-LoadCompHeatPumpController.idf

printf "Running AABB model with load compensation\n"
energyplus-24.2.0 -r -d out-dd-AABB-LC -D bungalow-2-heatpump-AABB-LoadCompHeatPumpController.idf

printf "Running AAAA model with weather compensation\n"
energyplus-24.2.0 -r -d out-dd-AAAA-WC -D bungalow-2-heatpump-AAAA-WeatherCompHeatPumpController.idf

printf "Running ABAB model with weather compensation\n"
energyplus-24.2.0 -r -d out-dd-ABAB-WC -D bungalow-2-heatpump-ABAB-WeatherCompHeatPumpController.idf

printf "Running AABB model with weather compensation\n"
energyplus-24.2.0 -r -d out-dd-AABB-WC -D bungalow-2-heatpump-AABB-WeatherCompHeatPumpController.idf
