# Longest Substring with Same Letters after Replacement (hard)
# https://www.educative.io/courses/grokking-the-coding-interview/R8DVgjq78yR
# 
# Given a string with lowercase letters only, if you are allowed to replace no more 
# than ‘k’ letters with any letter, find the length of the longest substring 
# having the same letters after replacement.

import collections

def length_of_longest_substring(chars, K):
  windowStart = 0
  max_size = 0
  longest_char_count = 0
  char_frequencies = collections.defaultdict(int)

  for windowEnd, char in enumerate(chars):
    char_frequencies[char] += 1

    longest_char_count = max(longest_char_count, char_frequencies[char])

    if ((windowEnd - windowStart + 1) - longest_char_count) > K:
      char_frequencies[windowStart] -= 1
      windowStart += 1

    max_size = max(max_size, windowEnd - windowStart + 1)
    
  return max_size