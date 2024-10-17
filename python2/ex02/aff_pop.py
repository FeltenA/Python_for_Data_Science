import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def expand_nbr(ser):
    """Replace number from series with equivalent float"""

    try:
        if isinstance(ser, pd.Series) and ser.shape[0] > 1:
            for i in range(2):
                nbr = ser.iloc[i]
                fnbr = float(nbr[:-1])
                if nbr.endswith("k"):
                    ser.iloc[i] = fnbr * 1000
                elif nbr.endswith("M"):
                    ser.iloc[i] = fnbr * 1000000
                elif nbr.endswith("B"):
                    ser.iloc[i] = fnbr * 1000000000
        return ser
    except Exception:
        return ser


def main():
    """Program that plots the populations of France and Belgium
    with data from the file population_total.csv"""

    data = load("population_total.csv")
    if data is None:
        exit(0)
    if "country" not in data.columns:
        print("AssertionError: CSV file not valid")
        exit(0)
    data = data.set_index("country")
    if all(x not in data.index for x in ["France", "Belgium"]):
        print("AssertionError: CSV file not valid")
        exit(0)
    plot_data = data.loc[["France", "Belgium"]].apply(expand_nbr)
    plot_data = plot_data.apply(pd.to_numeric, errors='coerce')
    if plot_data.isnull().values.any():
        print("AssertionError: CSV file not valid")
        exit(0)
    plot_data.drop(plot_data.loc[:, "2051":].columns, axis=1, inplace=True)
    plot_data.transpose().plot(color=['b', 'g'])
    plt.title("Population Projections")
    plt.legend(["Belgium", "France"], loc=4)
    plt.xlabel("Years")
    years = [x for x in plot_data.columns.to_list()[::40]]
    plt.xticks([int(x) - 1800 for x in years], years)
    plt.ylabel("Population")
    populations = ["20M", "40M", "60M"]
    plt.yticks([20000000, 40000000, 60000000], populations)
    plt.show()


if __name__ == "__main__":
    main()
