# Subarrays with Product Less than a Target (medium)
# https://www.educative.io/courses/grokking-the-coding-interview/RMV1GV1yPYz
# 
# Given an array with positive numbers and a target number, 
# find all of its contiguous subarrays whose product is less than the target number.

from collections import deque

def find_subarrays(arr, target):
  result = []

  trailing_product = 1
  windowStart = 0

  for windowEnd in range(len(arr)):
    trailing_product *= arr[windowEnd]

    while trailing_product >= target and windowStart <= windowEnd:
      trailing_product /= arr[windowStart]
      windowStart += 1

    q = deque()
    for i in reversed(range(windowStart, windowEnd + 1)):
      q.appendleft(arr[i])
      result.append(list(q))

  return result


def main():
  print(find_subarrays([2, 5, 3, 10], 30))
  print(find_subarrays([8, 2, 6, 5], 50))
  print(find_subarrays([60, 8, 2, 6, 5], 50))

main()