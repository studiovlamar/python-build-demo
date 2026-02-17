from utils import calculate_total

def test_calculate_total():
    assert calculate_total([10, 15, 25]) == 50
    assert calculate_total([]) == 0

# test care pica intentionat !
def test_calculate_total_fail():
    prices = [10, 20, 30]
    assert calculate_total(prices) == 999  
