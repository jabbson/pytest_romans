from multiprocessing.sharedctypes import Value
from sample import translate_decimal_to_roman
import pytest

def test_smallest():
    assert translate_decimal_to_roman(1) == "I", "1 should translate to I"

def test_largest():
    assert translate_decimal_to_roman(3999) == "MMMCMXCIX" "3999 should translate to 3999"

def test_invalid():
    with pytest.raises(ValueError):
        translate_decimal_to_roman(-10)