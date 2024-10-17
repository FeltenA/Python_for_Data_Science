import os
import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Opens a csv file and returns it as a dataframe"""

    try:
        if not isinstance(path, str):
            raise AssertionError("Bad Argument")
        elif not os.path.isfile(path):
            raise AssertionError("File does not exist")
        elif not path.lower().endswith(".csv"):
            raise AssertionError("File does not have the right file extension")
        data = pd.read_csv(path)
    except AssertionError as error:
        print("AssertionError:", error)
        return None

    print(f"Loading dataset of dimensions {data.shape}")
    return data
