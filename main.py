"""Application entrypoint that wires UI modes to sorting logic."""

from typing import List

from sorting_logic import bubble_sort, parse_numbers, swap_if_needed
from terminal_visualizer import bubble_sort_terminal_visual

DEFAULT_DELAY_SECONDS = 0.15


def run_pygame_mode(numbers: List[int], delay: float) -> List[int]:
    """Run the Pygame visualization mode and return the final values."""
    try:
        from pygame_visualizer import run_pygame_visualization
    except ImportError:
        print("Pygame is not installed. Install with: pip install pygame")
        return bubble_sort(numbers)

    delay_ms = int(max(0.0, delay) * 1000)
    return run_pygame_visualization(numbers, step_delay_ms=delay_ms)


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

    print("Choose visualization mode:")
    print("  n = no animation (plain sort)")
    print("  t = terminal ASCII animation")
    print("  p = Pygame 2D visualization")
    visual_mode = input("Mode [n/t/p]: ").strip().lower()

    if visual_mode in {"t", "p"}:
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

        if visual_mode == "t":
            sorted_numbers = bubble_sort_terminal_visual(numbers, frame_delay=delay)
        else:
            sorted_numbers = run_pygame_mode(numbers, delay)
    else:
        sorted_numbers = bubble_sort(numbers)

    print(f"\nFinal Sorted result: {sorted_numbers}")


if __name__ == "__main__":
    run_app()

    