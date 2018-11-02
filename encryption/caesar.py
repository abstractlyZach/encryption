import string
import operator

from . import base
from . import exceptions
from . import substitution


ALPHABET = list(string.ascii_lowercase)
INVALID_KEY_MESSAGE = 'Caesar cipher keys must be ints.'


def get_caesar_cipher():
    cipher = base.EncryptionScheme(
        caesar_encrypt,
        caesar_decrypt,
        is_valid_key
    )
    return cipher


def caesar_encrypt(plaintext, key):
    """Execute a Caesar encryption on the plaintext, translating each
    character x letters forward in the alphabet, where x is the key.
    """
    if not is_valid_key(key):
        raise exceptions.InvalidKeyException(INVALID_KEY_MESSAGE)
    translation_table = build_translation_table(key, operator.add)
    return substitution.substitute(plaintext, translation_table)


def caesar_decrypt(ciphertext, key):
    """Execute a Caesar decryption on the plaintext, translating each
    character x letters backward in the alphabet, where x is the key.
    """
    if not is_valid_key(key):
        raise exceptions.InvalidKeyException(INVALID_KEY_MESSAGE)
    translation_table = build_translation_table(key, operator.sub)
    return substitution.substitute(ciphertext, translation_table)


def build_translation_table(key, operation):
    """Build a translation table for a Caesar encrypt/decrypt operation.
    args:
        - key: a Caesar key (int)
        - operation: the operation to use when calculating the new
        translation. addition will make it count forward and subtraction
        will make it count backward when determining the new translated
        letter.

    """
    translation_table = dict()
    for index, original_letter in enumerate(ALPHABET):
        translated_letter_index = operation(index, key) % 26
        translation_table[original_letter] = ALPHABET[translated_letter_index]
    return translation_table


def is_valid_key(key):
    """Evaluate a key to see if it is a valid key for a Caesar cipher.
    """
    return isinstance(key, int)

