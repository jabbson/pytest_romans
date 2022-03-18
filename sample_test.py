from sample import to_roman
import pytest


@pytest.mark.parametrize(
    "input, output",
    [
        (1, "I"),
        (5, "V"),
        (10, "X"),
        (50, "L"),
        (100, "C"),
        (500, "D"),
        (1000, "M"),
    ]
)
def test_smallest_valid(input, output):
    assert to_roman(input) == output


def test_largest_valid():
    assert to_roman(3999) == "MMMCMXCIX", "3999 should translate to 3999"


def test_invalid_too_many_IXC():
    for v in ['IIII', 'XXXX', 'CCCC']:
        with pytest.raises(ValueError):
            to_roman(v)


def test_invalid_too_many_VLD():
    for v in ['VV', 'LL', 'DD']:
        with pytest.raises(ValueError):
            to_roman(v)


def test_invalid_not_a_num():
    with pytest.raises(ValueError):
        to_roman("string")


def test_invalid_zero():
    with pytest.raises(ValueError):
        to_roman(0)


def test_invalid_negative():
    with pytest.raises(ValueError):
        to_roman(-100)


def test_invalid_too_big():
    with pytest.raises(ValueError):
        to_roman(4000)
