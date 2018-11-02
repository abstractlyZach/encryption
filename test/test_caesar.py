import os

import pytest

from encryption import caesar
from encryption import exceptions
from encryption import utils


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


example_texts = (
    ('text'),
    [
        utils.get_text_as_string(file_name)
        for file_name in os.listdir('data')
        if file_name.endswith('.txt')
    ]
)

@pytest.mark.parametrize(*example_texts)
def test_caesar_cipher_encrypt_and_decrypt(text):
    cipher = caesar.get_caesar_cipher()
    expected = text
    key = 22
    encrypted = cipher.encrypt(text, key)
    actual = cipher.decrypt(encrypted, key)
    assert actual == expected



