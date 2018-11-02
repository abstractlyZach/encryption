import pytest

from encryption import caesar
from encryption import exceptions


def test_caesar_encrypt():
    plaintext = 'abc'
    expected = 'bcd'
    actual = caesar.caesar_encrypt(plaintext, 1)
    assert actual == expected


def test_caesar_decrypt():
    ciphertext = 'bcd'
    expected = 'abc'
    actual = caesar.caesar_decrypt(ciphertext, 1)
    assert actual == expected


def test_caesar_encrypt_raises_exception_on_invalid_key():
    plaintext = 'alskdfjalsdk'
    key = "I'm an invalid key!"
    with pytest.raises(exceptions.InvalidKeyException):
        caesar.caesar_encrypt(plaintext, key)


def test_caesar_decrypt_raises_exception_on_invalid_key():
    ciphertext = 'alskdfjalsdk'
    key = "I'm an invalid key!"
    with pytest.raises(exceptions.InvalidKeyException):
        caesar.caesar_decrypt(ciphertext, key)
