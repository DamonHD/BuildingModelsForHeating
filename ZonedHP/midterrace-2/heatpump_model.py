import pandas as pd
import altair as alt
import numpy as np

COP_REF=2.6
COP_REF_TEMP_C = 46.0
COP_HIGH = 2.3
COP_HIGH_TEMP_C = 51.5

COP_SLOPE = (COP_HIGH - COP_REF) / (COP_HIGH_TEMP_C - COP_REF_TEMP_C)
COP_INTERCEPT = COP_REF - COP_SLOPE * COP_REF_TEMP_C

# EIR = 1/COP
EIR_REF = 1/COP_REF
EIR_SLOPE = (1/COP_HIGH - 1/COP_REF) / (COP_HIGH_TEMP_C - COP_REF_TEMP_C)
EIR_INTERCEPT = 1/COP_REF - EIR_SLOPE * COP_REF_TEMP_C

# Multiplying the EIR coefficients by COP_REF gives a modifier curve
# where the EIR is 1.0 at COP_REF_TEMP_C
EIR_MOD_SLOPE = EIR_SLOPE * COP_REF
EIR_MOD_INTERCEPT = EIR_INTERCEPT * COP_REF

def temperatures(start=40.0, stop=55.0, num=100):
    return np.linspace(start, stop, num)

def linear_COP(t, slope=COP_SLOPE, intercept=COP_INTERCEPT):
    return slope * t + intercept

def linear_EIR(t, slope=EIR_SLOPE, intercept=EIR_INTERCEPT):
    return slope * t + intercept

def linear_EIR_mod(t, slope=EIR_MOD_SLOPE, intercept=EIR_MOD_INTERCEPT):
    return slope * t + intercept

def make_df(T, C):
    return pd.DataFrame().from_dict({"flow_temp": T, "CoP": C})

ts = temperatures()
df = make_df(ts, linear_COP(ts))
df["CoP_linEIR"] = 1/linear_EIR(ts)
df["CoP_linEIR_mod"] = 1/(EIR_REF * linear_EIR_mod(ts))

melt = df.melt("flow_temp")
melt
alt.Chart(melt).mark_line().encode(
    x="flow_temp",
    y=alt.Y("value", scale=alt.Scale(domain=(2.0, 3.0))),
    color="variable"
)

df["err_%"] = (df["CoP_linEIR"] - df["CoP"])/df["CoP"] * 100.0
df[df["err_%"] < 0].min()
