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
        "Environment:Site Outdoor Air Drybulb Temperature [C](Hourly)": "outdoor:air_temp_c",
        "Z1:Zone Air Temperature [C](Hourly)": "z1:air_temp_c",
        "Z2:Zone Air Temperature [C](Hourly)": "z2:air_temp_c",
        "Z3:Zone Air Temperature [C](Hourly)": "z3:air_temp_c",
        "Z4:Zone Air Temperature [C](Hourly)": "z4:air_temp_c",
        "Z1 RADIATOR:Baseboard Total Heating Rate [W](Hourly)": "z1:rad_power_w",
        "Z2 RADIATOR:Baseboard Total Heating Rate [W](Hourly)": "z2:rad_power_w",
        "Z3 RADIATOR:Baseboard Total Heating Rate [W](Hourly)": "z3:rad_power_w",
        "Z4 RADIATOR:Baseboard Total Heating Rate [W](Hourly)": "z4:rad_power_w",
        "Z1 RADIATOR:Baseboard Hot Water Mass Flow Rate [kg/s](Hourly)": "z1:mass_flow_kgps",
        "Z2 RADIATOR:Baseboard Hot Water Mass Flow Rate [kg/s](Hourly)": "z2:mass_flow_kgps",
        "Z3 RADIATOR:Baseboard Hot Water Mass Flow Rate [kg/s](Hourly)": "z3:mass_flow_kgps",
        "Z4 RADIATOR:Baseboard Hot Water Mass Flow Rate [kg/s](Hourly)": "z4:mass_flow_kgps",
        "Baseboard Total Heating Rate All Zones:PythonPlugin:OutputVariable [W](Hourly)": "total:rad_power_w",
        "HEAT PUMP:Heat Pump Load Side Heat Transfer Rate [W](Hourly)": "heat_pump:heat_gain_w",
        "HEAT PUMP:Heat Pump Electricity Rate [W](Hourly)": "heat_pump:electricity_w",
        "HEAT PUMP:Heat Pump Load Side Inlet Temperature [C](Hourly)": "heat_pump:return_temp_c",
        "HOT WATER LOOP:Plant Supply Side Outlet Temperature [C](Hourly)": "heat_pump:flow_temp_c",
        "SUPPLY PUMP:Pump Electricity Rate [W](Hourly)": "water_pump:electricity_w",
        "SUPPLY PUMP:Pump Fluid Heat Gain Rate [W](Hourly)": "water_pump:heat_gain_w",
        "SUPPLY PUMP:Pump Mass Flow Rate [kg/s](Hourly)": "water_pump:mass_flow_kgps",
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

    electricity = (
        summary[summary["variable"] == "electricity_w"].groupby("case")[["value"]].sum()
    )
    total_heat = (
        summary.loc[(summary.variable == "heat_gain_w"), ["case", "value"]]
        .groupby("case")
        .sum()
    )
    cop = total_heat / electricity

    electricity["variable"] = "electricity_w"
    electricity["location"] = "total"
    electricity.reset_index(inplace=True)
    total_heat["variable"] = "heat_gain_w"
    total_heat["location"] = "total"
    total_heat.reset_index(inplace=True)
    cop["variable"] = "COP (H4)"
    cop["location"] = "total"
    cop.reset_index(inplace=True)

    df = pd.concat([summary, electricity, total_heat, cop])

    return df


def format_summary(summary):
    summary = summary.set_index(["case", "variable", "location"]).unstack(0)
    summary = summary.reindex(
        [
            "air_temp_c",
            "rad_power_w",
            "mass_flow_kgps",
            "flow_temp_c",
            "return_temp_c",
            "heat_gain_w",
            "electricity_w",
            "COP (H4)",
        ],
        level=0,
    )
    summary = summary.reindex(
        ["outdoor", "z1", "z2", "z3", "z4", "heat_pump", "water_pump", "total"], level=1
    )
    return summary.droplevel(0, axis=1).reset_index()


def plot(summary):
    return alt.Chart(summary[summary.variable == "air_temp_c"]).mark_bar().encode(
        x="location", y="value", color="case", column="case"
    ).properties(title="Mean Zone Air Temperature (C)") & (
        alt.Chart(
            summary[(summary.variable == "rad_power_w") & (summary.location != "total")]
        )
        .mark_bar()
        .encode(
            x="location",
            y=alt.Y("value", scale=alt.Scale(domain=(0, 1800))),
            color="case",
            column="case",
        )
        .properties(title="Mean Zone Radiator Power Output (W)")
        | alt.Chart(
            summary[
                (
                    summary.variable.isin(["electricity_w", "rad_power_w"])
                    & (summary.location == "total")
                )
                | (summary.variable == "power_w")
            ].replace(
                {
                    "electricity_w": "Total Electricity",
                    "power_w": "Heat Pump Heat",
                    "rad_power_w": "Total Radiator Heat",
                }
            )
        )
        .mark_bar()
        .encode(
            x=alt.X(
                "variable",
                sort=["Total Electricity", "Heat Pump Heat", "Total Radiator Heat"],
            ),
            y=alt.Y("value", scale=alt.Scale(domain=(0, 1800))),
            color="case",
            column="case",
        )
        .properties(
            title="Mean Power Transfer (W)",
        )
    )


if __name__ == "__main__":
    format_summary(summarise(load_all(FILES))).to_markdown(
        "summary.md", index=False, floatfmt=".2f"
    )
