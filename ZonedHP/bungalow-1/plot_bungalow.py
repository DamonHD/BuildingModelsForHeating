import pandas as pd
from matplotlib import pyplot as plt


def load_results(
    test="out-dd/eplusout.csv",
    baseline="baseline/eplusout.csv",
):
    date_format = "%m/%d  %H:%M:%S"
    renamer = {
        "ZONE ONE:Zone Air Temperature [C](Hourly)": "air_temp_1_C",
        "ZONE ONE:Zone Air System Sensible Heating Energy [J](Hourly)": "heating_energy_1_J",
        "ZONE ONE:Zone Predicted Sensible Load to Setpoint Heat Transfer Rate [W](Hourly)": "heat_transfer_rate_1_W",
        "ZONE1BASEBOARD:Baseboard Total Heating Rate [W](Hourly)": "heating_rate_1_W",
        "RADIATOR:Baseboard Total Heating Rate [W](Hourly)": "heating_rate_1_W",
        "ZONE ONE PURCHASED AIR:Zone Ideal Loads Zone Total Heating Rate [W](Hourly)": "heating_rate_1_W",
    }

    test = (
        pd.read_csv(test, parse_dates=["Date/Time"], date_format=date_format)
        .rename(columns=lambda x: x.strip())
        .rename(columns=renamer)
    )
    baseline = (
        pd.read_csv(baseline, parse_dates=["Date/Time"], date_format=date_format)
        .rename(columns=lambda x: x.strip())
        .rename(columns=renamer)
    )

    return (test, baseline)


def plot(test, baseline):
    fig, axs = plt.subplots(nrows=2, ncols=2)

    def make_subplot(ax, test, baseline, title, add_legend=False):
        ax.set_title(title)
        ax.plot(baseline.index, baseline[title], label="baseline" if add_legend else "")
        ax.plot(test.index, test[title], label="test" if add_legend else "")

    make_subplot(axs[0, 0], test, baseline, "air_temp_1_C", True)
    make_subplot(
        axs[0, 1],
        test,
        baseline,
        "heating_energy_1_J",
    )
    make_subplot(
        axs[1, 0],
        test,
        baseline,
        "heat_transfer_rate_1_W",
    )

    make_subplot(
        axs[1, 1],
        test,
        baseline,
        "heating_rate_1_W",
    )

    fig.legend()

    plt.plot()
