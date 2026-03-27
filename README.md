# Bubble Sort Practice App

A Python app to learn Bubble Sort with two visualization modes:
- terminal ASCII animation
- Pygame 2D graphics animation

## What This Project Does

- Parses user input from comma-separated text into integers.
- Sorts numbers in ascending order using Bubble Sort.
- Uses an early-stop optimization when the list is already sorted.
- Supports in-place ASCII bar animation during sorting.
- Supports Pygame-based 2D bar animation during sorting.
- Shows every comparison step in visualization mode (not only swaps).
- Includes a basic pytest test suite with 5 tests.

## Files

- main.py: Thin application entry point and mode selection
- sorting_logic.py: Core sorting/parsing logic and visualization step generation
- terminal_visualizer.py: Terminal ASCII rendering UI
- pygame_visualizer.py: Pygame 2D rendering UI
- test_main.py: Pytest tests for core logic
- REPORT.md: Project reflection template/report notes
- JOURNAL.md: Running log of project interactions

## Requirements

- Python 3.10+
- Dependencies listed in `requirements.txt`

## Setup (Local Virtual Environment)

From the project folder:

```bash
python -m venv .venv
```

Activate the environment:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run The App

From the project folder:

```bash
python main.py
```

The app prompts for a mode:
- `n`: no animation (plain sort)
- `t`: terminal ASCII animation
- `p`: Pygame 2D visualization

If you choose terminal mode:
- It redraws the frame in place for animation-like output.
- It highlights the pair currently being compared.
- It supports custom animation delay in seconds.

If you choose Pygame mode:
- It opens a window with animated bars.
- It shows every comparison step.
- It supports runtime controls.

Example input:

```text
5, 1, 4, 2, 8
```

Expected output format:

```text
Sorted result: [1, 2, 4, 5, 8]
```

Sample animated frame meaning:
- `Action: COMPARE` means the pair was checked but not swapped.
- `Action: SWAP` means the pair was swapped.

## Pygame Controls

- `Space`: pause/resume
- `Up Arrow`: faster animation
- `Down Arrow`: slower animation
- `R`: restart playback
- `Esc`: close the visualization window

## Run Tests

```bash
python -m pytest -q
```

## Bubble Sort Notes

Bubble Sort repeatedly compares adjacent elements and swaps them when they are in the wrong order.

- Worst/Average time complexity: O(n^2)
- Best case (already sorted with early stop): O(n)
- Space complexity: O(1)

## Testing

Run tests with:

```bash
python -m pytest -q
```

## Notes

- ANSI cursor control is used for in-place redraw, with fallback behavior in unsupported terminals.
- Negative numbers are drawn with `-` bars and non-negative numbers with `#` bars.

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Possible Next Improvements

- Add input validation for empty values such as "1,,2".
- Add descending sort as an option.
- Add optional colorized markers for compared/swapped pairs.
