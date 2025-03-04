import pytest
from uv_demo.calculator import Calculator

@pytest.fixture
def calc():
    return Calculator(precision=2)

def test_add(calc):
    assert calc.add(2, 3) == 5.0
    assert calc.add(-1, 1) == 0.0
    assert calc.add(2.5, 3.7) == 6.2

def test_subtract(calc):
    # Test integer subtraction
    assert calc.subtract(5, 3) == 2.0
    assert calc.subtract(-5, -3) == -2.0
    assert calc.subtract(-5, 3) == -8.0
    assert calc.subtract(5, -3) == 8.0
    
    # Test with zeros
    assert calc.subtract(0, 0) == 0.0
    assert calc.subtract(5, 0) == 5.0
    assert calc.subtract(0, 5) == -5.0
    
    # Test decimal numbers
    assert calc.subtract(10.5, 3.2) == 7.3
    assert calc.subtract(3.14159, 2.0) == 1.14
    assert calc.subtract(99.99, 0.01) == 99.98
    
    # Test large numbers
    assert calc.subtract(1000000, 999999) == 1.0
    assert calc.subtract(-1000000, 1000000) == -2000000.0

def test_multiply(calc):
    assert calc.multiply(2, 3) == 6.0
    assert calc.multiply(-2, 3) == -6.0
    assert calc.multiply(2.5, 2) == 5.0

def test_divide(calc):
    assert calc.divide(6, 2) == 3.0
    assert calc.divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        calc.divide(5, 0)

def test_power(calc):
    assert calc.power(2, 3) == 8.0
    assert calc.power(3, 2) == 9.0
    assert calc.power(2, 0.5) == 1.41

def test_square_root(calc):
    assert calc.square_root(16) == 4.0
    assert calc.square_root(2) == 1.41
    with pytest.raises(ValueError):
        calc.square_root(-1)

def test_percentage(calc):
    assert calc.percentage(0.5) == 50.0
    assert calc.percentage(1) == 100.0
    assert calc.percentage(0.25) == 25.0

def test_memory_operations(calc):
    calc.add(2, 3)
    assert calc.get_last_result() == 5.0
    calc.clear_memory()
    assert calc.get_last_result() is None 