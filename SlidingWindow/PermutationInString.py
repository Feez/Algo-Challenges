# Permutation in a String (hard)
# https://www.educative.io/courses/grokking-the-coding-interview/N8vB7OVYo2D
# 
# Given a string and a pattern, find out if the string contains any 
# permutation of the pattern.

import collections

def find_permutation(chars, pattern):
  windowStart = 0
  pattern_counts = collections.defaultdict(int)
  for x in pattern:
    pattern_counts[x] += 1
  
  curr_counts = collections.defaultdict(int)
  pattern_len = len(pattern)

  for windowEnd, char in enumerate(chars):
    curr_counts[char] += 1

    window_len = (windowEnd - windowStart + 1)

    if window_len > pattern_len:
      if curr_counts[chars[windowStart]] == 1:
        del curr_counts[chars[windowStart]]
      else:
        curr_counts[chars[windowStart]] -= 1

      windowStart += 1

    if curr_counts == pattern_counts:
        return True

  return False