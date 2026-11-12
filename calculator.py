"""Арифметические операции калькулятора."""


def add(a, b):
    """Возвращает сумму двух чисел."""
    return a + b


def subtract(a, b):
    """Вычитает второе число из первого."""
    return a - b


def multiply(a, b):
    """Возвращает произведение двух чисел."""
    return a * b


def divide(a, b):
    """Делит первое число на второе.

    При нулевом делителе вызывает исключение ZeroDivisionError.
    """
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a / b
