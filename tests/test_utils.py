import os
import sys

# Ensure src/ is in the system path for imports
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

import numpy as np
import pytest

from src.utils.helpers import (  # Corrected import path
    calculate_moving_average,
    normalize_column,
)


def test_calculate_moving_average():
    data = [1, 2, 3, 4, 5]
    expected = [None, None, 2.0, 3.0, 4.0]
    result = calculate_moving_average(data, 3)
    assert result == expected


def test_normalize_column():
    data = [10, 20, 30, 40, 50]
    normalized = normalize_column(data)
    assert len(normalized) == len(data)
    np.testing.assert_almost_equal(sum(normalized), 0, decimal=5)
