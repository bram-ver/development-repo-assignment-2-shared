from src import read as rd
import numpy as np
import pytest


@pytest.mark.parametrize(
    "input_data_directory, input_data_name, expected_output",
    [
        (
            "data",
            "test1.t",
            np.array(
                [[0.0, 0.0, 0.0, 0.0], [0.1, 0.0, 0.0, 0.0], [0.2, 0.0, 0.0, 0.0]]
            ),
        )
    ],
)
def test_read_nump_data(input_data_directory, input_data_name, expected_output):
    """Test that tabular data is correctly read from a file and put into a numpy array."""
    assert np.array_equal(
        rd.read_nump_data(input_data_directory, input_data_name), expected_output
    )


def test_type_error_read_nump_data():
    """Test that a TypeError is raised when the path is not a string or Path."""
    with pytest.raises(TypeError):
        rd.read_nump_data(12, "test1.t")


def test_type_error_read_pandas_data():
    """Test that a TypeError is raised when the path is not a string or Path."""
    with pytest.raises(TypeError):
        rd.read_pandas_data(12, "test1.t")
