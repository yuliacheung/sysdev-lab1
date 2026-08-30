from math_utils import calculate_price

def test_calculate_total():
    assert calculate_price(12.5, 4) == 50.0
