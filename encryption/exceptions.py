"""Encryption exceptions"""

class InvalidKeyException(Exception):
    pass

class IncompleteKeyException(InvalidKeyException):
    pass

class InvalidEncryptionFunctionException(Exception):
    pass

class InvalidKeyValidationFunctionException(Exception):
    pass
