# Longest Substring with K Distinct Characters (medium)
# https://www.educative.io/courses/grokking-the-coding-interview/YQQwQMWLx80
# 
# Given a string, find the length of the longest substring in it with 
# no more than K distinct characters.

from collections import Counter

def longest_substring_with_k_distinct(chars, K):
  windowStart = 0
  counts = Counter()
  unique_chars = set()

  longest_count = 0

  for windowEnd in range(len(chars)):
    counts[chars[windowEnd]] += 1
    unique_chars.add(chars[windowEnd])

    #print(windowStart, windowEnd, "[" + ",".join(str(x) for x in unique_chars) + "]")
    #print(counts)

    if len(unique_chars) <= K:
      longest_count = max(longest_count, windowEnd - windowStart + 1)
    else:
      start_char = chars[windowStart]

      counts[start_char] -= 1
      if counts[start_char] == 0:
        unique_chars.remove(start_char)

      windowStart += 1

  return longest_count