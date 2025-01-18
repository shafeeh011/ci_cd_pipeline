from src.main import add, subtract

def test_add():
    assert add(1, 2) == 3
    assert add(2, 2) == 4
    assert add(3, 2) == 5

def test_subtract():
    assert subtract(1, 2) == -1 
    assert subtract(2, 2) == 0
    assert subtract(3, 2) == 1