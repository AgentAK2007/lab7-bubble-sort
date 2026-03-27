"""Terminal UI for Bubble Sort visualization."""

from __future__ import annotations

import os
import shutil
import time
from typing import List

from sorting_logic import generate_bubble_sort_steps

FALLBACK_CLEAR_LINES = 80
MIN_BAR_WIDTH = 10


def clear_and_home_cursor() -> None:
    """Clear terminal and move cursor to top-left for in-place redraw."""
    term = os.getenv("TERM", "")
    ansi_supported = term != "" or os.name != "nt"

    if ansi_supported:
        print("\033[2J\033[H", end="", flush=True)
    else:
        print("\n" * FALLBACK_CLEAR_LINES, end="", flush=True)


def get_bar_width_limit() -> int:
    """Get a safe bar width based on current terminal width."""
    terminal_width = shutil.get_terminal_size(fallback=(100, 30)).columns
    return max(MIN_BAR_WIDTH, terminal_width - 20)


def get_max_abs_value(values: List[int]) -> int:
    """Return max absolute value from the list, defaulting to 1."""
    return max((abs(value) for value in values), default=1)


def build_bar(value: int, max_val: int, terminal_width: int) -> str:
    """Return a scaled horizontal ASCII bar for one number."""
    safe_max = max(1, max_val)
    width = int(abs(value) / safe_max * terminal_width)
    width = max(1, width)
    char = "-" if value < 0 else "#"
    return char * width


def draw_frame(
    values: List[int],
    left_index: int,
    right_index: int,
    pass_num: int,
    comparison_count: int,
    swapped: bool,
) -> None:
    """Draw one terminal animation frame."""
    clear_and_home_cursor()
    frame_status = "SWAP" if swapped else "COMPARE"
    print("Bubble Sort In-Place Animation")
    print(
        f"Pass: {pass_num} | Comparison: {comparison_count} | Action: {frame_status}"
    )
    print("-" * 60)

    max_abs_val = get_max_abs_value(values)
    bar_width_limit = get_bar_width_limit()

    for index, value in enumerate(values):
        marker = "  "
        if index == left_index:
            marker = "->"
        elif index == right_index:
            marker = "<-"

        bar = build_bar(value, max_val=max_abs_val, terminal_width=bar_width_limit)
        print(f"{marker}[{index:02}] {value:>4} | {bar}")

    print("-" * 60)


def draw_final_frame(values: List[int], passes_completed: int, comparison_count: int) -> None:
    """Draw final terminal summary frame."""
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


def bubble_sort_terminal_visual(values: List[int], frame_delay: float) -> List[int]:
    """Animate Bubble Sort in terminal using generated logic steps."""
    delay = max(0.0, frame_delay)
    final_values = values[:]
    final_passes = 0
    final_comparisons = 0

    for step in generate_bubble_sort_steps(values):
        current_values = step["values"]
        final_values = current_values[:]
        final_passes = step["pass_num"]
        final_comparisons = step["comparison_count"]

        if step["done"]:
            break

        draw_frame(
            current_values,
            left_index=step["left"],
            right_index=step["right"],
            pass_num=step["pass_num"],
            comparison_count=step["comparison_count"],
            swapped=step["swapped"],
        )
        time.sleep(delay)

    draw_final_frame(final_values, final_passes, final_comparisons)
    values[:] = final_values
    return values
