"""Substition ciphers"""
from . import base
from . import exceptions


ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


class SubstitutionCipher(base.EncryptionScheme):
    """Cipher that replaces each letter of the plaintext with another
    specific letter of ciphertext."""
    def __init__(self):
        pass

    def encrypt(self, plaintext, key):
        self._validate_key(key)
        key = self._convert_key_to_lower(key)
        ciphertext = ''
        for char in plaintext:
            new_char = self._get_replacement_character(char, key)
            ciphertext += new_char
        return ciphertext

    def decrypt(self, ciphertext, encryption_key):
        self._validate_key(encryption_key)
        decryption_key = {value: key for key, value in encryption_key.items()}
        return self.encrypt(ciphertext, decryption_key)

    def _validate_key(self, encryption_key):
        self._check_keys_are_unique(encryption_key.keys())
        self._check_values_are_unique(encryption_key.values())

    def _check_keys_are_unique(self, keys):
        seen_keys = set()
        for key in keys:
            key = key.lower()
            if key in seen_keys:
                error_message = 'Key contains {} and {}'.format(key.upper(),
                                                                key.lower())
                raise exceptions.InvalidKeyException(error_message)
            else:
                seen_keys.add(key)

    def _check_values_are_unique(self, values):
        seen_values = set()
        for value in values:
            value = value.lower()
            if value in seen_values:
                error_message = 'Multiple chars are mapped to "{}"'.format(
                    value)
                raise exceptions.InvalidKeyException(error_message)
            else:
                seen_values.add(value)

    def _convert_key_to_lower(self, encryption_key):
        new_key = {key.lower(): value.lower()
                   for key, value in encryption_key.items()}
        return new_key

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


class CaesarCipher(SubstitutionCipher):
    def key_is_valid(self, key):
        return isinstance(key, int)

    def encrypt(self, plaintext, key):
        self._ensure_key_is_int(key)
        key = key % 26
        substitution_key = dict(zip(ALPHABET, ALPHABET[key:] + ALPHABET[:key]))
        return super(CaesarCipher, self).encrypt(plaintext, substitution_key)

    def decrypt(self, ciphertext, key):
        self._ensure_key_is_int(key)
        return self.encrypt(ciphertext, -key)

    # can't name _validate_key because then it'll interfere with the super call
    def _ensure_key_is_int(self, encryption_key):
        if not self.key_is_valid(encryption_key):
            error_message = "Key should be an int."
            raise exceptions.InvalidKeyException(error_message)


def get_caesar_cipher(shift_distance):
    """Returns a Caesar cipher.
    Args:
        - shift_distance: how far to shift each character. ex.
        shift_distance=1 means a->b, b->c, c->d, ...
        shift_distance=2 means a->c, b->d, c->e, ...
        shift_distance=-1 means a->z, b->a, c->b, ...
    Returns:
        SubstitutionCipher
    """
    pass



