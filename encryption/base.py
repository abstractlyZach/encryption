class EncryptionScheme(object):
    """Base class for encryption schemes."""
    def __init__(self):
        raise NotImplementedError

    def encrypt(self, plaintext, key):
        raise NotImplementedError

    def decrypt(self, ciphertext, key):
        raise NotImplementedError

    def key_is_valid(self, key):
        raise NotImplementedError
