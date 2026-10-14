"""Набор тестов для кодирования и декодирование шифром Цезаря. """

import unittest

from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere


class VigenreTestCase(unittest.TestCase):
    """ Тесты """

    def test_encrypt_vigenere_standard(self):
        self.assertEqual(encrypt_vigenere("PYTHON", "A"),"PYTHON")

    def test_encrypt_vigenere_not_letters(self):
        self.assertEqual(encrypt_vigenere("124?!", "X"),"124?!")

    def test_encrypt_vigenere_register(self):
        self.assertEqual(encrypt_vigenere("PyThOn", "R"),"GpKyFe")

    def test_decrypt_vigenere_standard(self):
        self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR","LEMON"),"ATTACKATDAWN")

    def test_decrypt_vigenere_not_letters(self):
        self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR123", "LEMON"), "ATTACKATDAWN123")

    def test_decrypt_vigenere_register(self):
        self.assertEqual(decrypt_vigenere("LxFoPvEfRnHr","LEMON"),"AtTaCkAtDaWn")

    def test_encrypt_vigenere_symmetry(self):
        self.assertEqual(decrypt_vigenere(encrypt_vigenere('PYTHON', 'bed'), 'bed'),"PYTHON")