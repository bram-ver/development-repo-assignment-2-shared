from matplotlib import pyplot as plt
import pandas as pd


def saveplot_pdf(path):
    """Save the plot"""
    if not path.endswith(".pdf"):
        raise ValueError("The file path must end with '.pdf'")
    plt.savefig(path)


def lineplot(
    df: pd.DataFrame,
    xcolumn: int = 0,
    dimensions: tuple = (10, 6),
    xlabel: str = None,
    ylabel: str = None,
    title: str = None,
    legend: bool = False,
):
    """Create a line plot for"""
    plt.figure(figsize=dimensions)
    for i in range(df.shape[1]):
        if i != xcolumn:
            plt.plot(df.iloc[:, xcolumn], df.iloc[:, i], label=df.columns[i])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    if legend:
        plt.legend()
