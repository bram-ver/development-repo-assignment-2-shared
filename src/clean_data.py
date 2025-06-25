
import pandas as pd
import numpy as np


def check_significant_data(df: pd.DataFrame, threshold=1e-10) -> pd.DataFrame:
    """
    Cleans the DataFrame by removing columns with variance below a specified threshold.

    Parameters:
    df (pd.DataFrame): The DataFrame to clean.
    threshold (float): The variance threshold below which columns will be removed.

    Returns:
    pd.DataFrame: The cleaned DataFrame with low-variance columns removed.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame.")
    
    variances = df.var()
    columns_to_keep = variances[variances > threshold].index
    return df[columns_to_keep]

def nan_to_zero_np(data: np.ndarray) -> np.ndarray:
    """
    Replaces NaN values in the DataFrame with zeros.

    Parameters:
    df (pd.DataFrame): The DataFrame to process.

    Returns:
    pd.DataFrame: The DataFrame with NaN values replaced by zeros.
    """
    data = np.nan_to_num(data)
    return data


# def clean_data_np(data: dict, threshold=1e-10) -> dict: