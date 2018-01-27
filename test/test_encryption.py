import pytest

from encryption import encryption

def test_init_raises_exception():
    with pytest.raises(NotImplementedError):
        encryption.EncryptionScheme()

def test_encrypt_raises_exception():
    with pytest.raises(NotImplementedError):
        encryption.EncryptionScheme.encrypt('self', 'abc', 'def')

def test_decrypt_raises_exception():
    with pytest.raises(NotImplementedError):
        encryption.EncryptionScheme.decrypt('self', 'abc', 'def')
