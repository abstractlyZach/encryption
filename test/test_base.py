import pytest

from encryption import base
from encryption import exceptions


def test_uncallable_encryption_function_raises_exception():
    with pytest.raises(exceptions.InvalidEncryptionFunctionException):
        base.EncryptionScheme(None, lambda x: x)


def test_uncallable_key_validation_function_raises_exception():
    with pytest.raises(exceptions.InvalidKeyValidationFunctionException):
        base.EncryptionScheme(lambda x: x, None)


def test_invalid_key_raises_exception():
    key_validation_function = lambda x: False
    encryption_function = lambda x, y: None
    encryption_scheme = base.EncryptionScheme(
        encryption_function, key_validation_function
    )
    with pytest.raises(exceptions.InvalidKeyException):
        encryption_scheme.encrypt('abc', 8)


def test_key_validation_function_gets_called(mocker):
    spy_function = mocker.MagicMock()
    scheme = base.EncryptionScheme(lambda x, y: None, spy_function)
    scheme.encrypt('abc', 4)
    spy_function.assert_called_once()

