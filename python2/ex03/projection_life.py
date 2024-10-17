import matplotlib.pyplot as plt
from load_csv import load


def main():
    """Plot relation between life expectancy and gross domestic product"""

    dt_life = load("life_expectancy_years.csv")
    dt_gdppc = load("income_per_person_gdppercapita\
_ppp_inflation_adjusted.csv")
    if dt_life is None or dt_gdppc is None:
        exit(0)
    if not all(x in dt_life.columns for x in ["country", "1900"]) or\
            not all(x in dt_gdppc.columns for x in ["country", "1900"]):
        print("AssertionError: CSV file not valid")
        exit(0)
    dt_life = dt_life.set_index("country", verify_integrity=True)
    dt_gdppc = dt_gdppc.set_index("country", verify_integrity=True)
    if dt_life is None or dt_gdppc is None:
        exit(0)
    ser_life = dt_life["1900"]
    ser_gdppc = dt_gdppc["1900"]

    plt.scatter(ser_gdppc, ser_life)
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    plt.show()


if __name__ == "__main__":
    main()
