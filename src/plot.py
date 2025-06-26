from matplotlib import pyplot as plt
import pandas as pd
from pathlib import Path


def saveplot_pdf(path: str | Path) -> None:
    """Save a plot as a PDF file.

    :Parameters:
        path (str or Path): File path where the plot will be saved.
        A plot should already be created before calling this function.

    :Exceptions:
        ValueError: If the path does not end with '.pdf' or if no plot has been created.

    :Returns:
        None. The function saves the current plot to the specified path."""
    if not path.endswith(".pdf"):
        raise ValueError("The file path must end with '.pdf'")
    if plt.get_fignums() == []:
        raise ValueError(
            "No plot has been created. Please create a plot before saving."
        )
    plt.savefig(path)


def lineplot(
    df: pd.DataFrame,
    xcolumn: int = 0,
    dimensions: tuple = (10, 6),
    xlabel: str = None,
    ylabel: str = None,
    title: str = None,
    legend: bool = False,
) -> None:
    """Create a line plot from a Pandas DataFrame.

    :Parameters:
        df: Pandas DataFrame containing the data to plot.
        xcolumn: Index of the column to use as the x-axis (default is 0).
        dimensions: Tuple specifying the dimensions of the plot (default is (10, 6)).
        xlabel: Label for the x-axis (default is None).
        ylabel: Label for the y-axis (default is None).
        title: Title of the plot (default is None).
        legend: Boolean indicating whether to show the legend (default is False).

    :Returns:
        None. The function creates a line plot and displays it.
    """
    plt.figure(figsize=dimensions)
    for i in range(df.shape[1]):
        if i != xcolumn:
            plt.plot(df.iloc[:, xcolumn], df.iloc[:, i], label=df.columns[i])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    if legend:
        plt.legend()
