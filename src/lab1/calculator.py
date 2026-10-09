"""Модуль калькулятора для выполнения арифметических операций."""


class Calculator:
    """Калькулятор для выполнения арифметических операций."""

    def addition(self, a: float, b: float) -> float:
        """Операция сложения."""
        return a + b

    def subtraction(self, a: float, b: float) -> float:
        """Операция вычитания."""
        return a - b

    def multiplication(self, a: float, b: float) -> float:
        """Операция умножения."""
        return a * b

    def division(self, a: float, b: float) -> float:
        """Операция деления."""
        return a / b

    def exponentiation(self, a: float, b: float) -> float:
        """Операция возведения в степень."""
        return a ** b