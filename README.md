# Bubble Sort Practice App

A Python console app to learn Bubble Sort with optional in-place terminal animation.

## What This Project Does

- Parses user input from comma-separated text into integers.
- Sorts numbers in ascending order using Bubble Sort.
- Uses an early-stop optimization when the list is already sorted.
- Supports in-place ASCII bar animation during sorting.
- Shows every comparison step in visualization mode (not only swaps).
- Includes a basic pytest test suite with 5 tests.

## Files

- main.py: Application logic and terminal visualization
- test_main.py: Pytest test cases
- REPORT.md: Project reflection template/report notes
- JOURNAL.md: Running log of project interactions

## Requirements

- Python 3.10+
- pytest (for tests)

## Run The App

From the project folder:

```bash
python main.py
```

The app will ask whether to enable in-place ASCII animation.

If you choose visualization mode:
- It redraws the frame in place for animation-like output.
- It highlights the pair currently being compared.
- It supports custom animation delay in seconds.

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

## Possible Next Improvements

- Add input validation for empty values such as "1,,2".
- Add descending sort as an option.
- Add optional colorized markers for compared/swapped pairs.
