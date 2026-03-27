"""Bubble Sort learning skeleton.

Fill in each TODO to build a complete Bubble Sort app.
Run this file often while you implement each step.
"""

from typing import List


def parse_numbers(raw_text: str) -> List[int]:
	"""Convert a comma-separated string into a list of integers.

	Example input: "5, 1, 4, 2, 8"
	Expected output: [5, 1, 4, 2, 8]
	"""
	# TODO 1:
	# 1) Split the string by comma
	# 2) Remove spaces around each item
	# 3) Convert each item to int
	# 4) Return the list of ints
	raise NotImplementedError("TODO 1: implement parse_numbers")


def swap_if_needed(values: List[int], index: int) -> bool:
	"""Compare neighbors at index and index + 1 and swap if needed.

	Returns:
		True if a swap happened, otherwise False.
	"""
	# TODO 2:
	# If values[index] > values[index + 1], swap them and return True.
	# Otherwise return False.
	raise NotImplementedError("TODO 2: implement swap_if_needed")


def bubble_sort(values: List[int]) -> List[int]:
	"""Sort values in ascending order using Bubble Sort.

	Keep this function in-place (modify the same list), then return it.
	"""
	n = len(values)

	# TODO 3:
	# Write the outer loop for passes.
	# Hint: after each pass, one more largest element is in final position.
	for _pass_num in range(0):
		swapped = False

		# TODO 4:
		# Write the inner loop range so it ignores the already-sorted tail.
		for i in range(0):
			# TODO 5:
			# Reuse swap_if_needed(values, i) here.
			did_swap = False
			if did_swap:
				swapped = True

		# TODO 6:
		# Early stop optimization:
		# if no swaps happened in this pass, stop the algorithm.
		if False:
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
		print("Invalid input. Use integers separated by commas.")
		return
	except NotImplementedError as exc:
		print(exc)
		return

	try:
		sorted_numbers = bubble_sort(numbers)
	except NotImplementedError as exc:
		print(exc)
		return

	print(f"Sorted result: {sorted_numbers}")


if __name__ == "__main__":
	run_app()
