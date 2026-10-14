"""Набор тестов для кодирования и декодирование шифром RSA. """

import unittest
from src.lab2.rsa import is_prime,decrypt,encrypt,gcd, generate_keypair,multiplicative_inverse
class RSATestCase(unittest.TestCase):
    """ Тесты """
    def test_RSA_prime(self):
        self.assertEqual(is_prime(17),True)

    def test_RSA_prime_false(self):
        self.assertEqual(is_prime(8),False)

    def test_RSA_gcd1(self):
        self.assertEqual(gcd(3,7),1)

    def test_RSA_gcd_zero(self):
        self.assertEqual(gcd(5,0),5)

    def test_RSA_gcd_zeroes(self):
        self.assertEqual(gcd(0,0),0)

    def test_RSA_gcd_eq(self):
        self.assertEqual(gcd(7,7),7)

    def test_RSA_gcd_standard(self):
        self.assertEqual(gcd(15,5),5)

    def test_RSA_multiplicative_inverse(self):
        self.assertEqual(multiplicative_inverse(3,11),4)

    def test_RSA_multiplicative_error(self):
        with self.assertRaises(ValueError):
            multiplicative_inverse(4,8)

    def test_rsa_full_cycle(self):
        public, private = generate_keypair(17, 19)
        original = "Love programming"
        cipher = encrypt(private, original)
        back = decrypt(public, cipher)
        self.assertEqual(back, original)