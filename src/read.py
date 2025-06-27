# from pathlib import Path


def read_nump_data(path, name, skip=1):
    """
    Reads a numpy data file and returns its content as a numpy array.

    Parameters:
    path (str or Path): The directory path where the file is located.
    name (str): The name of the file to read.
    skip (int): Number of lines to skip at the beginning of the file. Default is 1.
    """
    import numpy as np

    # if not isinstance(path, (str, Path)):
    #    raise TypeError("Path must be a string or a Path object.")
    file = f"{path}/{name}"
    return np.loadtxt(file, skiprows=skip)


def read_pandas_data(path, name):
    """
    Reads a pandas data file and returns its content as a pandas DataFrame.

    Parameters:
    path (str or Path): The directory path where the file is located.
    name (str): The name of the file to read.
    """
    import pandas as pd

    file = path / name
    return pd.read_csv(
        file, sep=r"\s+"
    )  # Using regex to handle whitespace as separator
