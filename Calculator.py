def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

def power(a, b):
    return a ** b

if __name__ == "__main__":
    print(add(5, 3))        # должно вывести 8
    print(subtract(10, 4))  # должно вывести 6
    print(multiply(7, 6))   # должно вывести 42
    print(divide(20, 4))    # должно вывести 5.0
    print(divide(10, 0))    # должно вывести "Ошибка: деление на ноль"
    print(power(2, 3))      # должно вывести 8