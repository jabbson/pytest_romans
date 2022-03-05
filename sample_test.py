from sample import to_roman
import pytest

def test_smallest_valid():
    assert to_roman(1) == "I", "1 should translate to I"

def test_largest_valid():
    assert to_roman(3999) == "MMMCMXCIX", "3999 should translate to 3999"

def test_invalid():
    with pytest.raises(ValueError):
        to_roman(0)

    with pytest.raises(ValueError):
        to_roman(-100)

    with pytest.raises(ValueError):
        to_roman(4000)
