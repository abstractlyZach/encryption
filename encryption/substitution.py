import collections

from . import exceptions


def substitute(text, key):
    """Substitute every character in the text for the letter that's
    specified in the key.
    """
    if key_is_invalid(key):
        raise exceptions.InvalidKeyException()
    result = ''
    for character in text:
        if character in key:
            result += key[character]
        else:
            result += character
    return result


def key_is_invalid(key):
    """Checks to make sure that a key is a one-to-one mapping stored as a
    dictionary.
    """
    if isinstance(key, dict):
        counter = collections.Counter(key.values())
        for value, count in counter.items():
            if count > 1:
                return True
        return False
    else:
        return True
