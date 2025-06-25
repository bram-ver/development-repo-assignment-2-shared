
from .read import read_nump_data, read_pandas_data
from .clean_data import check_significant_data, nan_to_zero_np
from .transform import get_wf
from pathlib import Path
import numpy as np

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
        self._extract_data()

        # Clean the data
        self.clean_data()

        # Extract time and wavefunction
        self.time, self.wf = get_wf(self.data['nstate_i'])

    def _extract_data(self):
        self.data['efield'] = read_nump_data(self.path, "efield.t")
        self.data['table'] = read_nump_data(self.path, "table.dat")
        self.data['nstate_i'] = read_nump_data(self.path, "nstate_i.t")
        self.data['expected'] = read_pandas_data(self.path, "expected.t")
        self.data['npop'] = read_pandas_data(self.path, "npop.t")

    def clean_data(self, threshold=1e-5):
        """
        Cleans the data by removing low-variance columns from the pandas DataFrames.
        
        Parameters:
        threshold (float): The variance threshold below which columns will be removed.
        """
        self.data['table'] = nan_to_zero_np(self.data['table'])

        self.data['expected'] = check_significant_data(self.data['expected'], threshold)
        self.data['npop'] = check_significant_data(self.data['npop'], threshold)
    



    

        