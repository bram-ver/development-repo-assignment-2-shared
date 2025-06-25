
from .read import read_nump_data, read_pandas_data
from .plot import plot_data
from pathlib import Path

class DynSym:
    """
    A class for handling dynamics simulation data.
    The input required is the path to the data directory.
    """

    files_pd = ["expected.t", "npop.t"]
    files_np = ["efield.t", "table.dat", "nstate_i.t"]

    def __init__(self, path):
        """
        Initializes the DynSym object with the given path.
        
        Parameters:
        path (str or Path): The directory path where the data files are located.
        """
        self.path = Path(path) if isinstance(path, str) else path
        if not isinstance(self.path, str):
            raise TypeError("Path must be a string or Path object.")
        if not self.path.exists():
            raise FileNotFoundError(f"Path '{self.path}' does not exist.")
        # Initialize the data
        self.data = {}
        self.data['efield'] = read_nump_data(self.path, "efield.t")
        self.data['table'] = read_nump_data(self.path, "table.dat")
        self.data['nstate_i'] = read_nump_data(self.path, "nstate_i.t")
        self.data['expected'] = read_pandas_data(self.path, "expected.t")
        self.data['npop'] = read_pandas_data(self.path, "npop.t")

        