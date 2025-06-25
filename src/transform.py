import numpy as np
def get_wf(wf):
        """
        Extracts the wavefunction data from the nstate_i file.
        """
        time = wf[0]  # First element is time
        wf = np.delete(wf, [0], axis=0) # Remove the time column
        # Convert to complex numbers
        real = wf[0::2]
        imag = wf[1::2]
        # Create complex wavefunction
        wf = real + 1j * imag
        return time, wf