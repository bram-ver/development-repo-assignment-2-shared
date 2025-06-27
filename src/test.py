""" This file is to test the functionalities in different modules."""

from plot import saveplot_pdf, lineplot
from transform import discrete_FT
import pandas as pd


def eliminate_columns(df, threshold=0.001):
    variances = df.var()
    columns_to_keep = variances[variances > threshold].index
    return df[columns_to_keep]


if __name__ == "__main__":
    df_efield = pd.read_csv("data/efield.t", delim_whitespace=True)
    df_efield = eliminate_columns(df_efield, threshold=0.0001)
    df_FT_efield = discrete_FT(df_efield["time"], df_efield["y"])
    lineplot(
        df_FT_efield, xlabel="frequency", ylabel="amplitude", title="FT", legend=True
    )
    saveplot_pdf("plots/FT.pdf")
