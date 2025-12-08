from ml_finance.scalper import find_place_value


def test_find_place_value_integer():
    assert find_place_value(10) == 0


def test_find_place_value_float():
    assert find_place_value(1.234) == 3


def test_find_place_value_trailing_zeroes_string():
    # strings preserve trailing zeros
    assert find_place_value("2.3400") == 4


def test_find_place_value_one_point_zero():
    # floats stringify to '1.0' so expect 1
    assert find_place_value(1.0) == 1
