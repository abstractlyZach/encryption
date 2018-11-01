"""Encryption exceptions"""

class InvalidKeyException(Exception):
    pass

class IncompleteKeyException(InvalidKeyException):
    pass

class NotAFunctionException(Exception):
    pass

class InvalidKeyValidationFunctionException(Exception):
    pass
