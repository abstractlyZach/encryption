from collections import defaultdict

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
    tokens = word_tokenize(ciphertext)
    for decryption_key in range(25):
        num_decrypted_words = count_decrypted_english_words(tokens,
                                                            decryption_key)
        hit_counter[decryption_key] = num_decrypted_words
    return hit_counter

def count_decrypted_english_words(tokens, decryption_key):
    cipher = substitution.CaesarCipher()
    tokens = [
        cipher.decrypt(token, decryption_key)
        for token in tokens
    ]
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
        hit counter for all keys up to return point.
        """
    hit_counter = defaultdict(int)
    tokens = word_tokenize(ciphertext)
    iteration_counter = 0
    while (iteration_counter * batch_size < len(tokens)):
        tokens_to_examine = tokens[iteration_counter * batch_size:
                                   (iteration_counter + 1)
                                                    * batch_size]
        for decryption_key in range(25):
            num_decrypted_words = count_decrypted_english_words(tokens_to_examine,
                                                                decryption_key)
            hit_counter[decryption_key] += num_decrypted_words
        best_key, second_best_key = get_best_two_keys(hit_counter)
        if hit_counter[best_key] > hit_counter[second_best_key] * threshold:
            return hit_counter
        iteration_counter += 1
    return hit_counter

def get_best_two_keys(hit_counter):
    sorted_keys = sorted(
        [decryption_key
         for decryption_key in hit_counter.keys()],
        key=lambda x: hit_counter[x])
    return sorted_keys[:2]



