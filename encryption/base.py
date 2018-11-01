from . import exceptions


class EncryptionScheme(object):
    """Base class for encryption schemes.
    """
    def __init__(
            self,
            encryption_function,
            decryption_function,
            key_validation_function
    ):
        """Load up the encryption scheme with an encryption function.
        """
        if callable(encryption_function):
            self._encryption_function = encryption_function
        else:
            raise exceptions.NotAFunctionException()
        if callable(decryption_function):
            self._decryption_function = decryption_function
        else:
            raise exceptions.NotAFunctionException()
        if callable(key_validation_function):
            self._key_validation_function = key_validation_function
        else:
            raise exceptions.InvalidKeyValidationFunctionException()

    def encrypt(self, plaintext, key):
        if self.key_is_valid(key):
            self._encryption_function(plaintext, key)
        else:
            raise exceptions.InvalidKeyException()

    def decrypt(self, ciphertext, key):
        if self.key_is_valid(key):
            self._decryption_function(ciphertext, key)
        else:
            raise exceptions.InvalidKeyException()

    def key_is_valid(self, key):
        return self._key_validation_function(key)

