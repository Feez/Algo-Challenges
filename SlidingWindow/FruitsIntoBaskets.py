# Fruits into Baskets (medium)
# https://www.educative.io/courses/grokking-the-coding-interview/Bn2KLlOR0lQ
# 
# Given an array of characters where each character represents a fruit tree, 
# you are given two baskets and your goal is to put maximum number of fruits in each basket. 
# The only restriction is that each basket can have only one type of fruit.
#
# You can start with any tree, but once you have started you can’t skip a tree. 
# You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
#
# Write a function to return the maximum number of fruits in both the baskets.

from collections import Counter

def fruits_into_baskets(fruits):
  windowStart = 0
  max_size = 0
  fruit_counts = Counter()

  for windowEnd, fruit in enumerate(fruits):
    fruit_counts[fruit] += 1

    while len(fruit_counts) > 2:
      curr = fruits[windowStart]
      if fruit_counts[curr] == 1:
        del fruit_counts[curr]
      else:
        fruit_counts[curr] -= 1

      windowStart += 1

    max_size = max(max_size, windowEnd - windowStart + 1)
    
  return max_size