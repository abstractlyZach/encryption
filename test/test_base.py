import pytest

from encryption import base

def test_init_raises_exception():
    with pytest.raises(NotImplementedError):
        base.EncryptionScheme()

def test_encrypt_raises_exception():
    with pytest.raises(NotImplementedError):
        base.EncryptionScheme.encrypt('self', 'abc', 'def')

def test_decrypt_raises_exception():
    with pytest.raises(NotImplementedError):
        base.EncryptionScheme.decrypt('self', 'abc', 'def')
