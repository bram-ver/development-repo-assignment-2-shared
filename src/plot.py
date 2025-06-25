"""
from matplotlib import pyplot as plt
import pandas as pd


def saveplot_pdf(path):
    "Save the plot"
    if not path.endswith(".pdf"):
        raise ValueError("The file path must end with '.pdf'")
    plt.savefig(path)
"""

"""def lineplot(
    df,
    numberoflines=1,
    dimensions=(10, 6),
    xlabel=None,
    ylabel=None,
    title=None,
    legend=None,
):
    plt.figure(figsize=dimensions)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend(legend)
    for i in range(numberoflines):
        plt.plot(df, df, label=''')
"""
