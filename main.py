"""Bubble Sort Application with Terminal Visualization."""

import os
import shutil
import time
from typing import List

DEFAULT_DELAY_SECONDS = 0.15
FALLBACK_CLEAR_LINES = 80
MIN_BAR_WIDTH = 10


def clear_and_home_cursor() -> None:
    """Clear terminal and move cursor to top-left for in-place redraw."""
    # Prefer ANSI in-place redraw. Fallback to simple line push if unsupported.
    term = os.getenv("TERM", "")
    ansi_supported = term != "" or os.name != "nt"

    if ansi_supported:
        print("\033[2J\033[H", end="", flush=True)
    else:
        print("\n" * FALLBACK_CLEAR_LINES, end="", flush=True)


def get_bar_width_limit() -> int:
    """Get a safe bar width based on current terminal width."""
    terminal_width = shutil.get_terminal_size(fallback=(100, 30)).columns
    # Reserve space for marker, index, value, and separators.
    return max(MIN_BAR_WIDTH, terminal_width - 20)


def build_bar(value: int, max_val: int = 10, terminal_width: int = 40) -> str:
    """Return a horizontal ASCII bar for one number, scaled to fit terminal."""
    if max_val == 0:
        max_val = 1

    # Scale width to fit terminal
    width = int(abs(value) / max_val * terminal_width)
    width = max(1, width)  # At least 1 char wide so zeros are visible.

    # Use different characters for negative numbers
    char = "-" if value < 0 else "#"
    return char * width


def get_max_abs_value(values: List[int]) -> int:
    """Return max absolute value from the list, defaulting to 1."""
    return max((abs(value) for value in values), default=1)


def draw_frame(
    values: List[int],
    left_index: int,
    right_index: int,
    pass_num: int,
    comparison_count: int,
    swapped: bool,
) -> None:
    """Draw one animation frame for the current Bubble Sort comparison."""
    clear_and_home_cursor()
    frame_status = "SWAP" if swapped else "COMPARE"
    print("Bubble Sort In-Place Animation")
    print(
        f"Pass: {pass_num + 1} | Comparison: {comparison_count} | Action: {frame_status}"
    )
    print("-" * 60)

    # Find max for scaling
    max_abs_val = get_max_abs_value(values)
    bar_width_limit = get_bar_width_limit()

    for index, value in enumerate(values):
        # Marker for the two elements currently being compared
        marker = "  "
        if index == left_index:
            marker = "->"
        elif index == right_index:
            marker = "<-"

        bar = build_bar(value, max_val=max_abs_val, terminal_width=bar_width_limit)
        print(f"{marker}[{index:02}] {value:>4} | {bar}")

    print("-" * 60)


def bubble_sort_visual(values: List[int], frame_delay: float) -> List[int]:
    """Bubble Sort with per-comparison in-place terminal redraw."""
    n = len(values)
    delay = max(0.0, frame_delay)
    comparison_count = 0
    passes_completed = 0

    for pass_num in range(n - 1):
        passes_completed = pass_num + 1
        swapped_in_pass = False

        for i in range(n - 1 - pass_num):
            comparison_count += 1
            did_swap = swap_if_needed(values, i)
            if did_swap:
                swapped_in_pass = True

            draw_frame(
                values,
                left_index=i,
                right_index=i + 1,
                pass_num=pass_num,
                comparison_count=comparison_count,
                swapped=did_swap,
            )
            time.sleep(delay)

        if not swapped_in_pass:
            break

    # Final Summary Frame
    clear_and_home_cursor()
    print("Bubble Sort: ANIMATION COMPLETE")
    print(f"Total Passes: {passes_completed} | Total Comparisons: {comparison_count}")
    print("-" * 60)
    
    max_abs_val = get_max_abs_value(values)
    bar_width_limit = get_bar_width_limit()
    for index, value in enumerate(values):
        bar = build_bar(value, max_val=max_abs_val, terminal_width=bar_width_limit)
        print(f"  [{index:02}] {value:>4} | {bar}")
    print("-" * 60)

    return values


def parse_numbers(raw_text: str) -> List[int]:
    """Convert a comma-separated string into a list of integers."""
    if not raw_text.strip():
        raise ValueError("Input cannot be empty")

    return [int(x.strip()) for x in raw_text.split(",")]


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

    visual_mode = input("Use in-place ASCII animation? (y/n): ").strip().lower()

    if visual_mode == "y":
        speed_input = input(
            f"Enter animation delay in seconds (default {DEFAULT_DELAY_SECONDS}): "
        ).strip()
        try:
            delay = float(speed_input)
        except ValueError:
            delay = DEFAULT_DELAY_SECONDS

        if delay < 0:
            print(f"Negative delay is not valid. Using {DEFAULT_DELAY_SECONDS} seconds.")
            delay = DEFAULT_DELAY_SECONDS

        sorted_numbers = bubble_sort_visual(numbers, frame_delay=delay)
    else:
        sorted_numbers = bubble_sort(numbers)

    print(f"\nFinal Sorted result: {sorted_numbers}")


if __name__ == "__main__":
    run_app()