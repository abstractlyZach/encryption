"""Substition ciphers"""
from . import base

class SubstitutionCipher(base.EncryptionScheme):
    def __init__(self, key):
        self._key = key
