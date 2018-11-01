import pytest

from encryption import base
from encryption import exceptions


def dummy_function(*args):
    return

def test_uncallable_encryption_function_raises_exception():
    with pytest.raises(exceptions.NotAFunctionException):
        base.EncryptionScheme(None, dummy_function, dummy_function)

def test_uncallable_decryption_function_raises_exception():
    with pytest.raises(exceptions.NotAFunctionException):
        base.EncryptionScheme(dummy_function, None, dummy_function)

def test_uncallable_key_validation_function_raises_exception():
    with pytest.raises(exceptions.InvalidKeyValidationFunctionException):
        base.EncryptionScheme(dummy_function, dummy_function, None)


def test_invalid_key_raises_exception():
    key_validation_function = lambda x: False
    encryption_function = dummy_function
    decryption_function = dummy_function
    encryption_scheme = base.EncryptionScheme(encryption_function,
                                              decryption_function,
                                              key_validation_function)
    with pytest.raises(exceptions.InvalidKeyException):
        encryption_scheme.encrypt('abc', 8)


def test_key_validation_function_gets_called(mocker):
    spy_function = mocker.MagicMock()
    scheme = base.EncryptionScheme(dummy_function, dummy_function,
                                   spy_function)
    scheme.encrypt('abc', 4)
    spy_function.assert_called_once()

