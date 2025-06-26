import numpy as np
import pandas as pd


def get_wf(wf):
    """
    Extracts the wavefunction data from the nstate_i file.
    """
    time = wf[0]  # First element is time
    wf = np.delete(wf, [0], axis=0)  # Remove the time column
    # Convert to complex numbers
    real = wf[0::2]
    imag = wf[1::2]
    # Create complex wavefunction
    wf = real + 1j * imag
    return time, wf


def discrete_FT(time_series, amplitudes):
    freq = np.fft.rfftfreq(len(time_series), d=(time_series[1] - time_series[0]))
    amp = np.fft.rfft(amplitudes)
    transformed = pd.DataFrame({"frequency": freq, "amplitude": np.abs(amp)})
    return transformed
