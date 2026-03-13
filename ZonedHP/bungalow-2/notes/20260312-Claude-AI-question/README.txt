Claude was asked why the expected heat loss was not being seen for the AAAA-WC model, copied here.

(Claude Opus 4.6 extended research mode, ~18 minutes run-time.)

Question:
Why, given the fabric U-values, the steady-state heat loss on design day for this model is not exactly 2kW: 
https://github.com/DamonHD/BuildingModelsForHeating/blob/main/ZonedHP/bungalow-2/bungalow-2-heatpump-AAAA-WeatherCompHeatPumpController.idf

Answer:
See Answer.md

Initial observations:
  * Claude seems to be claiming heat loss is *higher* than 2kW: it is *lower* here.
  * Claude claims all sorts of additional loss factors such as infiltration and solar gain
    which have been carefully arranged to be zero.

Superficially this seems to be wrong and mainly unhelpful,
but a more thorough reading may yield some helpful elements,
even if just verifying the claimed additional loss factors to be absent.

The most useful take-away is a reminder that there will have to be some fudge factors
to get an E+ model system results close to the idealised Java conduction-only model.