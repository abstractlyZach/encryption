import pytest

from encryption import exceptions
from encryption import substitution


ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

@pytest.fixture
def substitution_cipher():
    return substitution.SubstitutionCipher()

class TestSubstitutionCipher(object):
    def test_init(self):
        key = {}
        substitution.SubstitutionCipher()

    def test_symbols_dont_change_if_not_in_key(self, substitution_cipher):
        cipher = substitution_cipher
        plaintext = '!@#$;,. '
        ciphertext = cipher.encrypt(plaintext, {})
        assert plaintext == ciphertext

    def test_symbols_change_if_in_key(self, substitution_cipher):
        plaintext = '!@#$:,. "'
        key = {'!': 'a'}
        ciphertext = substitution_cipher.encrypt(plaintext, key)
        assert ciphertext == 'a' + plaintext[1:]

    def test_unrecognized_char_throws_exception(self, substitution_cipher):
        plaintext = 'abcdefghijkl'
        key = {}
        with pytest.raises(exceptions.IncompleteKeyException):
            substitution_cipher.encrypt(plaintext, key)

    def test_full_alphabet(self, substitution_cipher):
        plaintext = 'abcdefghijklmnopqrstuvwxyz'
        key = dict(zip(plaintext, plaintext[1:] + plaintext[0]))
        ciphertext = substitution_cipher.encrypt(plaintext, key)
        assert ciphertext == plaintext[1:] + plaintext[0]

    def test_two_chars_mapped_to_same_char_throws_exception(self,
                                                         substitution_cipher):
        plaintext = ''
        key = {'a': 'b', 'b': 'b'}
        with pytest.raises(exceptions.InvalidKeyException):
            substitution_cipher.encrypt(plaintext, key)

    def test_key_is_valid(self, substitution_cipher):
        key = dict(zip(ALPHABET, ALPHABET))
        assert substitution_cipher.key_is_valid(key)

    def test_key_is_invalid(self, substitution_cipher):
        key = {'a': 'b', 'b': 'b'}
        assert not substitution_cipher.key_is_valid(key)


