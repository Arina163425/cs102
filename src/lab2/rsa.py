
"""Реализация алгоритма шифрования RSA."""

import random
import typing as tp


def is_prime(number: int) -> bool:
    """
    Tests to see if a number is prime.
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    if number < 2:
        return False

    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False

    return True


def gcd(first_number: int, second_number: int) -> int:
    """
    Euclid's algorithm for determining the greatest common divisor.
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    if first_number == 0:
        return second_number

    if second_number == 0:
        return first_number

    while first_number != second_number:
        if first_number > second_number:
            first_number = first_number - second_number
        else:
            second_number = second_number - first_number

    return first_number


def multiplicative_inverse(exponent: int, phi: int) -> int:
    """
    Find the modular multiplicative inverse.
    >>> multiplicative_inverse(7, 40)
    23
    """
    for inverse in range(1, phi):
        if (exponent * inverse) % phi == 1:
            return inverse

    raise ValueError("Обратное число не существует")


def generate_keypair(
    first_prime: int, second_prime: int
) -> tp.Tuple[tp.Tuple[int, int], tp.Tuple[int, int]]:
    """Генерирует открытый и закрытый ключи RSA."""

    if not (is_prime(first_prime) and is_prime(second_prime)):
        raise ValueError("Both numbers must be prime.")

    if first_prime == second_prime:
        raise ValueError("p and q cannot be equal")

    # n = pq
    modulus = first_prime * second_prime

    # phi = (p-1)(q-1)
    phi = (first_prime - 1) * (second_prime - 1)

    # Choose an integer e such that e and phi(n) are coprime
    public_exponent = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are coprime
    greatest_divisor = gcd(public_exponent, phi)

    while greatest_divisor != 1:
        public_exponent = random.randrange(1, phi)
        greatest_divisor = gcd(public_exponent, phi)

    # Generate the private key
    private_exponent = multiplicative_inverse(public_exponent, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return (
        (public_exponent, modulus),
        (private_exponent, modulus)
    )


def encrypt(key_pair: tp.Tuple[int, int], plaintext: str) -> tp.List[int]:
    """Шифрует сообщение с использованием ключа RSA."""

    # Unpack the key into its components
    key, modulus = key_pair

    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % modulus for char in plaintext]

    # Return the array of bytes
    return cipher


def decrypt(key_pair: tp.Tuple[int, int], ciphertext: tp.List[int]) -> str:
    """Расшифровывает сообщение с использованием ключа RSA."""

    # Unpack the key into its components
    key, modulus = key_pair

    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % modulus) for char in ciphertext]

    # Return the array of bytes as a string
    return "".join(plain)


if __name__ == "__main__":
    print("RSA Encrypter/ Decrypter")

    input_prime = int(input("Enter a prime number (17, 19, 23, etc): "))
    input_second_prime = int(
        input("Enter another prime number (Not one you entered above): ")
    )

    print("Generating your public/private keypairs now . . .")

    public, private = generate_keypair(input_prime, input_second_prime)

    print("Your public key is ", public, " and your private key is ", private)

    message = input("Enter a message to encrypt with your private key: ")

    encrypted_msg = encrypt(private, message)

    print("Your encrypted message is: ")
    print("".join(map(str, encrypted_msg)))

    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))
