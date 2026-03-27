"""Core Bubble Sort logic with no UI dependencies."""

from __future__ import annotations

from typing import Iterator, List, TypedDict


class SortStep(TypedDict):
    """A single visualization step for Bubble Sort."""

    values: List[int]
    left: int
    right: int
    pass_num: int
    comparison_count: int
    swapped: bool
    done: bool


def parse_numbers(raw_text: str) -> List[int]:
    """Convert a comma-separated string into a list of integers."""
    if not raw_text.strip():
        raise ValueError("Input cannot be empty")

    return [int(item.strip()) for item in raw_text.split(",")]


def swap_if_needed(values: List[int], index: int) -> bool:
    """Swap adjacent items when values[index] is greater than values[index + 1]."""
    if values[index] > values[index + 1]:
        values[index], values[index + 1] = values[index + 1], values[index]
        return True
    return False


def bubble_sort(values: List[int]) -> List[int]:
    """Sort the list in place in ascending order and return it."""
    n = len(values)
    for pass_num in range(n - 1):
        swapped = False
        for i in range(n - 1 - pass_num):
            if swap_if_needed(values, i):
                swapped = True
        if not swapped:
            break
    return values


def generate_bubble_sort_steps(initial_values: List[int]) -> Iterator[SortStep]:
    """Yield Bubble Sort states for each comparison and a final summary step."""
    values = initial_values[:]
    n = len(values)
    comparison_count = 0
    passes_completed = 0

    if n < 2:
        yield {
            "values": values,
            "left": -1,
            "right": -1,
            "pass_num": 0,
            "comparison_count": 0,
            "swapped": False,
            "done": True,
        }
        return

    for pass_num in range(n - 1):
        passes_completed = pass_num + 1
        swapped_in_pass = False

        for i in range(n - 1 - pass_num):
            comparison_count += 1
            did_swap = swap_if_needed(values, i)
            if did_swap:
                swapped_in_pass = True

            yield {
                "values": values[:],
                "left": i,
                "right": i + 1,
                "pass_num": pass_num + 1,
                "comparison_count": comparison_count,
                "swapped": did_swap,
                "done": False,
            }

        if not swapped_in_pass:
            break

    yield {
        "values": values[:],
        "left": -1,
        "right": -1,
        "pass_num": passes_completed,
        "comparison_count": comparison_count,
        "swapped": False,
        "done": True,
    }
