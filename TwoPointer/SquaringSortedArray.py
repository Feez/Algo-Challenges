# Squaring a Sorted Array (easy)
# https://www.educative.io/courses/grokking-the-coding-interview/R1ppNG3nV9R
# 
# Given a sorted array, create a new array containing squares of all 
# the number of the input array in the sorted order.

def make_squares(arr):
  squares = []
  
  first_negative = -1

  for i in reversed(range(len(arr))):
    if arr[i] < 0:
      first_negative = i
      break

  left_p = first_negative
  right_p = first_negative + 1

  for i in range(len(arr)):
    if left_p >= 0 and right_p < len(arr):
      left_val = arr[left_p] * arr[left_p]
      right_val = arr[right_p] * arr[right_p]
      if left_val > right_val:
        squares.append(right_val)
        right_p += 1
      else:
        squares.append(left_val)
        left_p -= 1
    elif left_p >= 0:
      squares.append(arr[left_p] * arr[left_p])
      left_p -= 1
    else:
      squares.append(arr[right_p] * arr[right_p])
      right_p += 1

  return squares