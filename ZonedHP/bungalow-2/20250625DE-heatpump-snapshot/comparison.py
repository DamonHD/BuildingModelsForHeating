import pandas as pd
# from matplotlib import pyplot as plt
import altair as alt

FILES = {
    "aaaa": "out-dd-AAAA/eplusout.csv",
    "abab": "out-dd-ABAB/eplusout.csv",
    "aabb": "out-dd-AABB/eplusout.csv",
}


def load_file(name, file):
    renamer = {
        "Date/Time": "time",
        "Z1:Zone Air Temperature [C](Hourly)": "z1:air_temp_c",
        "Z2:Zone Air Temperature [C](Hourly)": "z2:air_temp_c",
        "Z3:Zone Air Temperature [C](Hourly)": "z3:air_temp_c",
        "Z4:Zone Air Temperature [C](Hourly)": "z4:air_temp_c",
        "Z1 RADIATOR:Baseboard Total Heating Rate [W](Hourly)": "z1:rad_power_w",
        "Z2 RADIATOR:Baseboard Total Heating Rate [W](Hourly)": "z2:rad_power_w",
        "Z3 RADIATOR:Baseboard Total Heating Rate [W](Hourly)": "z3:rad_power_w",
        "Z4 RADIATOR:Baseboard Total Heating Rate [W](Hourly)": "z4:rad_power_w",
        "HEAT PUMP:Heat Pump Load Side Heat Transfer Rate [W](Hourly)": "heat_pump:power_w",
        "HEAT PUMP:Heat Pump Electricity Rate [W](Hourly)": "heat_pump:electricity_w",
        "SUPPLY PUMP:Pump Electricity Rate [W](Hourly)": "water_pump:electricity_w",
    }

    df = pd.read_csv(file).rename(columns=lambda x: x.strip()).rename(columns=renamer)
    df["case"] = name
    df["time"] = df["time"].str.replace("  24:", "  00:")
    df["time"] = pd.to_datetime(df["time"], format=" %m/%d   %H:%M:%S")

    # 1st winter design day only
    df = df.iloc[:50]
    df = df[df["time"] <= "1900-01-16"]

    # Tidy
    df = df.melt(["time", "case"])
    df[["location", "variable"]] = df.variable.str.split(":", n=1, expand=True)

    return df


def load_all(files):
    return pd.concat(load_file(k, v) for k, v in files.items())


def summarise(df):
    summary = df.drop(columns="time").groupby(["case", "variable", "location"]).mean()
    summary = summary.reset_index()

    rad_power = summary[summary["variable"]=="rad_power_w"].groupby("case")[["value"]].sum()
    rad_power["variable"] = "rad_power_w"
    rad_power["location"] = "total"
    rad_power.reset_index(inplace=True)
    rad_power

    electricity = summary[summary["variable"]=="electricity_w"].groupby("case")[["value"]].sum()
    electricity["variable"] = "electricity_w"
    electricity["location"] = "total"
    electricity.reset_index(inplace=True)

    return pd.concat([summary, rad_power, electricity])

# electricity = electricity.set_index(["variable", "location"], append=True)
# summary = summary.unstack(0)
# summary.columns = summary.columns.droplevel(0)

summary.set_index(["case", "variable", "location"]).unstack(0)

def plot(summary):
    return alt.Chart(summary[summary.variable=="air_temp_c"]).mark_bar().encode(
        x = "location",
        y= "value",
        color = "case",
        column="case"
    ).properties(title="Mean Zone Air Temperature (C)") & (
        alt.Chart(summary[(summary.variable=="rad_power_w") & (summary.location != "total")]).mark_bar().encode(
            x = "location",
            y= alt.Y("value", scale=alt.Scale(domain=(0,1800))),
            color = "case",
            column="case"
        ).properties(
            title="Mean Zone Radiator Power Output (W)"
        ) | alt.Chart(
            summary[(summary.variable.isin(["electricity_w", "rad_power_w"]) & (summary.location=="total")) | (summary.variable=="power_w")]
                .replace({"electricity_w": "Total Electricity", "power_w": "Heat Pump Heat", "rad_power_w": "Total Radiator Heat"})
        ).mark_bar().encode(
            x=alt.X("variable", sort=["Total Electricity", "Heat Pump Heat", "Total Radiator Heat"]),
            y= alt.Y("value", scale=alt.Scale(domain=(0,1800))),
            color="case",
            column="case",
        ).properties(
            title="Mean Power Transfer (W)",
        )
    )
