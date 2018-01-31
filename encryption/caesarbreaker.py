from nltk.tokenize import word_tokenize

from . import substitution
from . import utils

ENGLISH_DICTIONARY = utils.get_english_dictionary()


def brute_force(ciphertext):
    """Try all 26 different keys and return the most-likely one."""
    hit_counter = dict()
    for decryption_key in range(25):
        num_decrypted_words = count_decrypted_words(ciphertext, decryption_key)
        hit_counter[decryption_key] = num_decrypted_words
    return get_key_with_biggest_value(hit_counter)

def count_decrypted_words(ciphertext, decryption_key):
    cipher = substitution.CaesarCipher()
    plaintext = cipher.decrypt(ciphertext, decryption_key)
    tokens = word_tokenize(plaintext)
    return count_number_of_english_words(tokens)

def count_number_of_english_words(tokens):
    num_english_words = 0
    for token in tokens:
        if token in ENGLISH_DICTIONARY:
            num_english_words += 1
    return num_english_words

def get_key_with_biggest_value(dictionary):
    return max(dictionary.keys(), key=lambda x: dictionary[x])

