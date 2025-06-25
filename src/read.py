from pathlib import Path
def read_nump_data(path, name, skip=1):
    """
    Reads a numpy data file and returns its content as a numpy array.
    
    Parameters:
    path (str or Path): The directory path where the file is located.
    name (str): The name of the file to read.
    skip (int): Number of lines to skip at the beginning of the file. Default is 1.
    """
    import numpy as np
    if not Path(path).exists():
        raise FileNotFoundError(f"The specified path {path} does not exist.")
    if not (Path(path) / name).exists():
        raise FileNotFoundError(f"The file {name} does not exist in the specified path {path}.")
    path = Path(path) if not isinstance(path, Path) else path
    file = path / name
    return np.loadtxt(file, skiprows=skip)


def read_pandas_data(path, name):
    """
    Reads a pandas data file and returns its content as a pandas DataFrame.
    
    Parameters:
    path (str or Path): The directory path where the file is located.
    name (str): The name of the file to read.
    """
    import pandas as pd
    # Error handling for file not found
    if not Path(path).exists():
        raise FileNotFoundError(f"The specified path {path} does not exist.")
    if not (Path(path) / name).exists():
        raise FileNotFoundError(f"The file {name} does not exist in the specified path {path}.")
    path = Path(path) if not isinstance(path, Path) else path
    file = path / name
    return pd.read_csv(file, sep=r"\s+")  # Using regex to handle whitespace as separator
