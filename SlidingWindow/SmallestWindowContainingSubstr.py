# Smallest Window containing Substring (hard)
# https://www.educative.io/courses/grokking-the-coding-interview/3wDJAYG2pAR
# 
# Given a string and a pattern, find the smallest substring in the given string 
# which has all the characters of the given pattern.

import collections

def find_substring(chars, pattern):
  windowStart = 0
  pattern_counts = collections.defaultdict(int)
  matched = 0

  for pattern_char in pattern:
    pattern_counts[pattern_char] += 1

  min_length = len(chars) + 1
  substr_start = 0

  for windowEnd, char in enumerate(chars):
    if char in pattern_counts:
      pattern_counts[char] -= 1

      if pattern_counts[char] >= 0:
        matched += 1

    while matched == len(pattern):
      curr_window_len = (windowEnd - windowStart + 1)
      if min_length > curr_window_len:
        substr_start = windowStart
        min_length = curr_window_len

      left_char = chars[windowStart]
      if left_char in pattern_counts:
        if pattern_counts[left_char] == 0:
          matched -= 1
        pattern_counts[left_char] += 1
      
      windowStart += 1

  if min_length > len(chars):
    return ""
  return chars[substr_start : substr_start + min_length]