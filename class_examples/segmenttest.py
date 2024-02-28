import pytest

from apps.class_examples.invalidnumbererror import InvalidNumberError
from apps.class_examples.sevensegmentdisplay import is_on, is_valid, get_shape_of_index_one_and_five, \
    get_shape_of_index_two_and_four, get_index_zero, get_index_four, get_index_seven


def test_is_off_when_last_index_is_not_zero():
    assert is_on("12233456") is False
    assert is_on("12234500")


def test_is_valid():
    with pytest.raises(InvalidNumberError) as error:
        is_valid("190897800")
    assert error.type == InvalidNumberError
    with pytest.raises(InvalidNumberError) as error:
        is_valid("11209087")
    assert error.type == InvalidNumberError
    with pytest.raises(InvalidNumberError) as error:
        is_valid("00101")
    assert error.type == InvalidNumberError
    assert is_valid("00000001")



def test_valid_number_return_shapes():
    assert get_shape_of_index_one_and_five("11010011") == f" {"#":>5}" + f"\n {"#":>5}"
    assert get_shape_of_index_one_and_five("10010111") == f"#{" ":>5}" + f"\n#{" ":>5}"
    assert get_shape_of_index_one_and_five("11010111") == f"#{"#":>5}" + f"\n#{"#":>5}"
    assert get_shape_of_index_one_and_five("10010011") == f" {" ":>5}" + f"\n {" ":>5}"


def test_valid_number_return_shapes_index_two_four():
    assert get_shape_of_index_two_and_four("00101000") == f"#{"#":>5}" + f"\n#{"#":>5}"
    assert get_shape_of_index_two_and_four("00010000") == f" {" ":>5}" + f"\n {" ":>5}"
    assert get_shape_of_index_two_and_four("00001000") == f"#{" ":>5}" + f"\n#{" ":>5}"
    assert get_shape_of_index_two_and_four("10110011") == f" {"#":>5}" + f"\n {"#":>5}"


def test_valid_numbers_return_shapes_index_one():
    assert get_index_zero("10000010") == f"{"#"*6}"
    assert get_index_zero("00000010") == f"{" ":>6}"


def test_valid_numbers_return_shapes_index_four():
    assert get_index_four("00010010") == f"{"#" * 6}"
    assert get_index_four("00000010") == f"{" ":>6}"


def test_valid_numbers_return():
    assert get_index_seven("00010010") == f"{"#" * 6}"
    assert get_index_seven("00000000") == f"{" " * 6}"
