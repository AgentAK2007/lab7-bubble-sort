"""Bubble Sort Application."""

from typing import List

def parse_numbers(raw_text: str) -> List[int]:
    """Convert a comma-separated string into a list of integers."""
    return [int(x.strip()) for x in raw_text.split(',')]

def swap_if_needed(values: List[int], index: int) -> bool:
    """Compare neighbors at index and index + 1 and swap if needed."""
    if values[index] > values[index + 1]:
        values[index], values[index + 1] = values[index + 1], values[index]
        return True
    return False

def bubble_sort(values: List[int]) -> List[int]:
    """Sort values in ascending order using Bubble Sort."""
    n = len(values)
    for pass_num in range(n - 1):
        swapped = False
        for i in range(n - 1 - pass_num):
            did_swap = swap_if_needed(values, i)
            if did_swap:
                swapped = True
        if not swapped:
            break
    return values

def run_app() -> None:
    """Simple console app to test your Bubble Sort implementation."""
    print("Bubble Sort Practice App")
    print("Enter numbers separated by commas (example: 5, 1, 4, 2, 8)")
    user_input = input("Numbers: ")

    try:
        numbers = parse_numbers(user_input)
    except ValueError:
        print("Invalid input please use integers separated by commas.")
        return

    sorted_numbers = bubble_sort(numbers)
    print(f"Sorted result: {sorted_numbers}")

if __name__ == "__main__":
    run_app()