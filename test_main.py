import pytest

from sorting_logic import bubble_sort, parse_numbers, swap_if_needed


def test_parse_numbers_valid_csv_input() -> None:
    assert parse_numbers("5, 1, 4, 2, 8") == [5, 1, 4, 2, 8]


def test_parse_numbers_invalid_input_raises_value_error() -> None:
    with pytest.raises(ValueError):
        parse_numbers("1, two, 3")


def test_swap_if_needed_swaps_and_returns_true() -> None:
    values = [9, 3]
    did_swap = swap_if_needed(values, 0)

    assert did_swap is True
    assert values == [3, 9]


def test_bubble_sort_sorts_unsorted_list() -> None:
    values = [5, 1, 4, 2, 8]
    assert bubble_sort(values) == [1, 2, 4, 5, 8]


def test_bubble_sort_handles_duplicates_and_negatives() -> None:
    values = [3, -1, 3, 0, -1]
    assert bubble_sort(values) == [-1, -1, 0, 3, 3]
