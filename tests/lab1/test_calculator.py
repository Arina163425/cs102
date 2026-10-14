"""Модуль для тестирования арифметических операций калькулятора."""

import unittest

from src.lab1.calculator import Calculator


class CalculatorTestCase(unittest.TestCase):
    """Тесты для проверки работы класса Calculator."""

    def setUp(self):
        """Создаёт объект калькулятора перед каждым тестом."""
        self.calc = Calculator()

    def test_addition(self):
        """Проверяет правильность операции сложения."""
        self.assertEqual(self.calc.addition(2, 3), 5)

    def test_subtraction(self):
        """Проверяет правильность операции вычитания."""
        self.assertEqual(self.calc.subtraction(5, 3), 2)

    def test_multiplication(self):
        """Проверяет правильность операции умножения."""
        self.assertEqual(self.calc.multiplication(2, 3), 6)

    def test_division(self):
        """Проверяет правильность операции деления."""
        self.assertEqual(self.calc.division(6, 3), 2)

    def test_exponentiation(self):
        """Проверяет правильность возведения в степень."""
        self.assertEqual(self.calc.exponentiation(2, 3), 8)

    def test_division_by_zero(self):
        """Проверяет возникновение ошибки при делении на ноль."""
        with self.assertRaises(ZeroDivisionError):
            self.calc.division(10, 0)
