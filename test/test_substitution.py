import pytest

from encryption import substitution
from encryption import exceptions


invalid_key_parameters = (
    ('key'),
    [
        {'a': 'c', 'b': 'c'},
        {'c': 'd', 'e': 'd', 'f': 'd'},
        'test string',
        None,
        set()
    ]
)

@pytest.mark.parametrize(*invalid_key_parameters)
def test_invalid_key_raises_exception(key):
    text = ''
    with pytest.raises(exceptions.InvalidKeyException):
        substitution.substitute(text, key)


def test_doesnt_throw_exception_on_empty_arguments():
    substitution.substitute('', dict())

def test_substitutes_single_character():
    key = {'a': 'b'}
    text = 'a'
    expected = 'b'
    actual = substitution.substitute(text, key)
    assert actual == expected


def test_substitutes_multiple_characters():
    key = {'a': 'b'}
    text = 'aaa'
    expected = 'bbb'
    actual = substitution.substitute(text, key)
    assert actual == expected


def test_substitutes_only_defined_characters():
    key = {'z': 'y'}
    text = 'zzxxyy'
    expected = 'yyxxyy'
    actual = substitution.substitute(text, key)
    assert actual == expected
