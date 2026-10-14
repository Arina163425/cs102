def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    alf = "abcdefghijklmnopqrstuvwxyz"
    shift = [alf.index(i.lower()) for i in keyword]
    k = 0
    for i in ciphertext:
        if i.lower() not in alf:
            plaintext += i
        elif i == i.lower():
            index = (alf.index(i) - shift[k]) % 26
            plaintext += alf[index]
        else:
            index = (alf.index(i.lower()) - shift[k]) % 26
            plaintext += alf[index].upper()
        if i.lower() in alf:
            k += 1
            if k == len(shift):
                k = 0

    # PUT YOUR CODE HERE
    return plaintext


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """

    ciphertext = ""
    alf = "abcdefghijklmnopqrstuvwxyz"

    shift = [alf.index(i.lower()) for i in keyword]
    k = 0
    for i in plaintext:
        if i.lower() not in alf:
            ciphertext += i
        elif i == i.lower():
            index = (alf.index(i) + shift[k]) % 26
            ciphertext += alf[index]
        else:
            index = (alf.index(i.lower()) + shift[k]) % 26
            ciphertext += alf[index].upper()
        if i.lower() in alf:
            k += 1
            if k == len(shift):
                k = 0



    # PUT YOUR CODE HERE
    return ciphertext