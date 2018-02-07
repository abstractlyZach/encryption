from nltk.tokenize import word_tokenize

from . import substitution
from . import utils

ENGLISH_DICTIONARY = utils.get_english_dictionary()


def break_and_get_best_key(breaker_function, ciphertext):
    hit_counter = breaker_function(ciphertext)
    return get_key_with_biggest_value(hit_counter)

def brute_force(ciphertext):
    """Try all 26 different keys and return the word count for each key."""
    hit_counter = dict()
    for decryption_key in range(25):
        num_decrypted_words = count_decrypted_words(ciphertext, decryption_key)
        hit_counter[decryption_key] = num_decrypted_words
    return hit_counter

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


def incremental_brute_force(ciphertext, batch_size, threshold=2):
    """Brute force the ciphertext in batches. Once the number of hits in the
    first-place key exceeds the second-place key by the given threshold,
    return the first-place key.
    Args:
        - ciphertext: text to decipher
        - batch_size: number of tokens to brute force at a time
        - threshold: return when 1st-place hits > 2nd-place hits * threshold
    Returns:
        key
        """
    hit_counter = dict()
    pass
