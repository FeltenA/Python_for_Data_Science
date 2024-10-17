import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def main():
    """Program that plots the life expectancy of France with data
    from the file life_expectancy_years.csv"""

    data = load("life_expectancy_years.csv")
    if data is None:
        exit(0)
    if "country" not in data.columns:
        print("AssertionError: CSV file not valid")
        exit(0)
    data = data.set_index("country")
    if "France" not in data.index:
        print("AssertionError: CSV file not valid")
        exit(0)
    num_check = data.loc["France"].apply(pd.to_numeric, errors='coerce')
    if num_check.isnull().values.any():
        print("AssertionError: CSV file not valid")
        exit(0)
    data.loc["France"].plot()
    plt.title("France Life expectancy Projections")
    plt.xlabel("Years")
    years = [x for x in data.loc["France"].index.to_list()[::40]]
    plt.xticks([int(x) - 1800 for x in years], years)
    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == "__main__":
    main()
