from Calculator import add, subtract, multiply, divide

def test_add():
    assert add(5, 3) == 8
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(5, 5) == 0
    assert subtract(0, 10) == -10

def test_multiply():
    assert multiply(7, 6) == 42
    assert multiply(5, 0) == 0
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(20, 4) == 5.0
    assert divide(10, 2) == 5.0
    assert divide(10, 0) == "Ошибка: деление на ноль"