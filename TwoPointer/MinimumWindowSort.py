# Minimum Window Sort (medium)
# https://www.educative.io/courses/grokking-the-coding-interview/N8rOAP6Lmw6
#
# Given an array, find the length of the smallest subarray in it which
# when sorted will sort the whole array.


def shortest_window_sort(arr):
    # Empty or single element array is already sorted
    if len(arr) <= 1:
        return 0

    left = 0
    right = 1
    first_diff = None
    last_diff = None

    while right < len(arr):
        if arr[left] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]

            if first_diff is None:
                first_diff = left

            last_diff = right

        left += 1
        right += 1

    # If no diff found, already sorted
    if first_diff is None:
        return 0

    min_val = arr[first_diff]
    max_val = arr[first_diff]

    for i in range(first_diff, last_diff + 1):
        min_val = min(min_val, arr[i])
        max_val = max(max_val, arr[i])

    # Extend first_diff to include elements greater than minimum
    while first_diff > 0 and arr[first_diff - 1] > min_val:
        first_diff -= 1

    # Extend last_diff to include elements less than maximum
    while last_diff < len(arr) - 1 and arr[last_diff + 1] < max_val:
        last_diff += 1

    return (last_diff - first_diff + 1)

print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12])) # Expected: 5
print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))    # Expected: 5
print(shortest_window_sort([1, 2, 3]))                  # Expected: 0
print(shortest_window_sort([3, 2, 1]))                  # Expected: 3
print(shortest_window_sort([2, 6, 4, 8, 10, 9, 15]))    # Expected: 5
