from ml_finance.utils import simple_moving_average


def test_sma_basic():
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    sma = simple_moving_average(data, window=3)
    assert sma[0] is None
    assert sma[1] is None
    assert sma[2] == (1.0 + 2.0 + 3.0) / 3
    assert sma[3] == (2.0 + 3.0 + 4.0) / 3
    assert sma[4] == (3.0 + 4.0 + 5.0) / 3


def test_sma_empty():
    assert simple_moving_average([], window=3) == []


import pytest


def test_sma_invalid_window():
    with pytest.raises(ValueError):
        simple_moving_average([1, 2, 3], window=0)
