import unittest
from src.lab2.caesar import decrypt_caesar,encrypt_caesar
class caesarTestCase(unittest.TestCase):

    def test_encrypt_caesar(self):
        self.assertEqual(encrypt_caesar('PYTHOn123', 3), 'SBWKRq123')

    def test_decrypt_caesar(self):
        self.assertEqual(decrypt_caesar('SBWKrQ345', 3), 'PYTHoN345')

    def test_cyrrilic_symbols(self):
        self.assertAlmostEqual(encrypt_caesar("золото спрятано под старцем",3),"золото спрятано под старцем")

