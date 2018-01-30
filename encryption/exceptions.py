"""Encryption exceptions"""

class InvalidKeyException(Exception):
    pass

class IncompleteKeyException(InvalidKeyException):
    pass

