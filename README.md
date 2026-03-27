# Bubble Sort Practice App

A small Python console app to learn and practice Bubble Sort.

## What This Project Does

- Parses user input from comma-separated text into integers.
- Sorts numbers in ascending order using Bubble Sort.
- Uses an early-stop optimization when the list is already sorted.
- Includes a basic pytest test suite with 5 tests.

## Files

- main.py: Application code (parsing, swap helper, bubble sort, CLI runner)
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

Example input:

```text
5, 1, 4, 2, 8
```

Expected output format:

```text
Sorted result: [1, 2, 4, 5, 8]
```

## Run Tests

```bash
python -m pytest -q
```

## Bubble Sort Notes

Bubble Sort repeatedly compares adjacent elements and swaps them when they are in the wrong order.

- Worst/Average time complexity: O(n^2)
- Best case (already sorted with early stop): O(n)
- Space complexity: O(1)

## Learning Ideas

- Add input validation for empty values such as "1,,2".
- Add descending sort as an option.
- Print the list after each pass to visualize sorting.
