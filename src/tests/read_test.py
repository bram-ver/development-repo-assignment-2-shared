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
    assert np.array_equal(
        rd.read_nump_data(input_data_directory, input_data_name), expected_output
    )
