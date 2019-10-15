# Dutch National Flag Problem (medium)
# https://www.educative.io/courses/grokking-the-coding-interview/RMBxV6jz6Q0
# 
# Given an array containing 0s, 1s and 2s, sort the array in-place. 

# https://coderbyte.com/algorithm/dutch-national-flag-sorting-problem

def dutch_flag_sort(arr):
  low = 0
  mid = 0
  high = len(arr) - 1

  while mid <= high:
    curr = arr[mid]

    if curr == 0:
      arr[mid], arr[low] = arr[low], arr[mid]
      low += 1
      mid += 1
    elif curr == 1:
      mid += 1
    else:
      arr[mid], arr[high] = arr[high], arr[mid]
      high -= 1

  print(arr)
