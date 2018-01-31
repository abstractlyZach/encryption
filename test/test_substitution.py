import pytest

from encryption import exceptions
from encryption import substitution


ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
FOX_TEXT = 'The quick brown fox jumps over the lazy dog.'
SHIFT_1 = 'Uif rvjdl cspxo gpy kvnqt pwfs uif mbaz eph.'
SHIFT_25 = 'Sgd pthbj aqnvm enw itlor nudq sgd kzyx cnf.'

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

    def test_key_maps_different_plain_to_same_cipher(self,
                                                     substitution_cipher):
        key = {'a': 'b', 'b': 'b'}
        assert not substitution_cipher.key_is_valid(key)

    def test_case_stays_same(self, substitution_cipher):
        plaintext = 'The QUICK broWn FoX'
        key = dict(zip(plaintext.lower(), plaintext.lower()))
        ciphertext = substitution_cipher.encrypt(plaintext, key)
        assert plaintext == ciphertext

    def test_uppercase_in_key_doesnt_affect_encryption(self,
                                                       substitution_cipher):
        plaintext = 'AaCc'
        key = {'A': 'b', 'c': 'D'}
        ciphertext = substitution_cipher.encrypt(plaintext, key)
        assert ciphertext == 'BbDd'

    def test_multiple_keys_with_same_char_in_both_cases(self,
                                                        substitution_cipher):
        key = {'a': 'b', 'A': 'c'}
        assert not substitution_cipher.key_is_valid(key)

    def test_multiple_values_with_same_char_in_both_cases(self,
                                                          substitution_cipher):
        key = {'a': 'b', 'b': 'B'}
        assert not substitution_cipher.key_is_valid(key)

    def test_decrypt(self, substitution_cipher):
        key = {'a': 'b', 'b': 'c', 'c': 'd'}
        ciphertext = 'bcd'
        plaintext = substitution_cipher.decrypt(ciphertext, key)
        assert plaintext == 'abc'



class TestCaesarCipher(object):
    def test_no_shift(self):
        cipher = substitution.CaesarCipher()
        plaintext = FOX_TEXT
        ciphertext = cipher.encrypt(plaintext, 0)
        assert plaintext == ciphertext

    def test_shift_1(self):
        cipher = substitution.CaesarCipher()
        plaintext = FOX_TEXT
        ciphertext = cipher.encrypt(plaintext, 1)
        assert ciphertext == SHIFT_1

    def test_shift_26(self):
        cipher = substitution.CaesarCipher()
        plaintext = FOX_TEXT
        ciphertext = cipher.encrypt(plaintext, 26)
        assert ciphertext == plaintext

    def test_shift_27(self):
        cipher = substitution.CaesarCipher()
        plaintext = FOX_TEXT
        ciphertext = cipher.encrypt(plaintext, 27)
        assert ciphertext == SHIFT_1

    def test_shift_back_1(self):
        cipher = substitution.CaesarCipher()
        plaintext = FOX_TEXT
        ciphertext = cipher.encrypt(plaintext, -1)
        assert ciphertext == SHIFT_25

    def test_shift_back_26(self):
        cipher = substitution.CaesarCipher()
        plaintext = FOX_TEXT
        ciphertext = cipher.encrypt(plaintext, -26)
        assert ciphertext == plaintext

    def test_shift_back_27(self):
        cipher = substitution.CaesarCipher()
        plaintext = FOX_TEXT
        ciphertext = cipher.encrypt(plaintext, -27)
        assert ciphertext == SHIFT_25

    def test_key_is_valid(self):
        valid_keys = [-100, 100, 0]
        invalid_keys = [{'a':'b', 'b':'c'}, 'aeiou', []]
        cipher = substitution.CaesarCipher()
        for key in valid_keys:
            assert cipher.key_is_valid(key)
        for key in invalid_keys:
            assert not cipher.key_is_valid(key)

    def test_shift_raises_exception_with_invalid_key(self):
        cipher = substitution.CaesarCipher()
        with pytest.raises(exceptions.InvalidKeyException):
            cipher.encrypt('abc', {'a':'b', 'b':'c'})

    def test_decrypt_1(self):
        cipher = substitution.CaesarCipher()
        ciphertext = SHIFT_1
        plaintext = cipher.decrypt(ciphertext, 1)
        assert plaintext == FOX_TEXT

    def test_decrypt_25(self):
        cipher = substitution.CaesarCipher()
        ciphertext = SHIFT_25
        plaintext = cipher.decrypt(ciphertext, 25)
        assert plaintext == FOX_TEXT

    def test_decrypt_neg_1(self):
        cipher = substitution.CaesarCipher()
        ciphertext = SHIFT_25
        plaintext = cipher.decrypt(ciphertext, -1)
        assert plaintext == FOX_TEXT

    def test_decrypt_neg_25(self):
        cipher = substitution.CaesarCipher()
        ciphertext = SHIFT_1
        plaintext = cipher.decrypt(ciphertext, -25)
        assert plaintext == FOX_TEXT
