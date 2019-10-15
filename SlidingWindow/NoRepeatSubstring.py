# No-repeat Substring (hard)
# https://www.educative.io/courses/grokking-the-coding-interview/YMzBx1gE5EO
# 
# Given a string, find the length of the longest substring which 
# has no repeating characters.

def non_repeat_substring(chars):
  windowStart = 0
  curr_chars = set()
  max_size = 0

  for windowEnd in range(len(chars)):
      while chars[windowEnd] in curr_chars:
          curr_chars.discard(chars[windowStart])
          windowStart += 1

      curr_chars.add(chars[windowEnd])
      max_size = max(max_size, windowEnd - windowStart + 1)

  return max_size