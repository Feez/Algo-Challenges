# Merge Intervals (medium)
# https://www.educative.io/courses/grokking-the-coding-interview/3jyVPKRA8yx
#
# Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

from __future__ import print_function

class interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def is_overlap(a, b):
  start = max(a.start, b.start)
  end = min(a.end, b.end)

  return end - start >= 0

def get_max_interval(a, b):
  start = min(a.start, b.start)
  end = max(a.end, b.end)

  return interval(start, end)

def merge(intervals):
  if len(intervals) == 0:
    return []

  intervals.sort(key=lambda x : x.start)

  merged = [intervals[0]]
  
  for i in range(1, len(intervals)):
    curr = intervals[i]

    if is_overlap(curr, merged[-1]):
      merged[-1] = get_max_interval(curr, merged[-1])
    else:
      merged.append(curr)

  return merged

def main():
  print("Merged intervals: ", end='')
  for i in merge([interval(1, 4), interval(2, 5), interval(7, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([interval(6, 7), interval(2, 4), interval(5, 9)]):
    i.print_interval()
  print()

  print("Merged intervals: ", end='')
  for i in merge([interval(1, 4), interval(2, 6), interval(3, 5)]):
    i.print_interval()
  print()

main()
