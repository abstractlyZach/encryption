"""Substition ciphers"""
from . import base
from . import exceptions

class SubstitutionCipher(base.EncryptionScheme):
    """Cipher that replaces each letter of the plaintext with another
    specific letter of ciphertext."""
    def __init__(self):
        pass

    def encrypt(self, plaintext, key):
        self._validate_key(key)
        ciphertext = ''
        for char in plaintext:
            new_char = self._get_replacement_character(char, key)
            ciphertext += new_char
        return ciphertext

    def _validate_key(self, key):
        seen_values = set()
        for _, value in key.items():
            if value in seen_values:
                error_message = 'Multiple chars are mapped to "{}"'.format(
                    value)
                raise exceptions.InvalidKeyException(error_message)
            else:
                seen_values.add(value)

    def _get_replacement_character(self, char, key):
        try:
            if char.isupper():
                return key[char.lower()].upper()
            else:
                return key[char]
        except KeyError:
            return self._handle_missing_character(char)

    def _handle_missing_character(self, char):
        if char.isalpha():
            error_message = 'Key does not have a mapping for "{}"'.format(char)
            raise exceptions.IncompleteKeyException(error_message)
        else:
            return char

    def key_is_valid(self, key):
        try:
            self._validate_key(key)
        except exceptions.InvalidKeyException:
            return False
        return True




