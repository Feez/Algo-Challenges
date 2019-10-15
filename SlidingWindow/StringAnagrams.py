# String Anagrams (hard)
# https://www.educative.io/courses/grokking-the-coding-interview/YQ8N2OZq0VM
# 
# Given a string and a pattern, find all anagrams of the pattern in the given string.
#
# Anagrams of 'abc' : (1) 'abc', (2) 'acb', (3) 'baac', (4) 'bca', (5) 'cab', (6) 'cba'.
#
# Note: Very similar to 'PermutationInString'

import collections

def find_string_anagrams(chars, pattern):
  windowStart = 0
  pattern_counts = collections.defaultdict(int)
  for x in pattern:
    pattern_counts[x] += 1
  
  curr_counts = collections.defaultdict(int)
  pattern_len = len(pattern)

  results = []

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
        results.append(windowStart)

  return results