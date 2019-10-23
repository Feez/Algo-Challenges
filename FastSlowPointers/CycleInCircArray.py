# Cycle in a Circular Array (hard)
# https://www.educative.io/courses/grokking-the-coding-interview/3jY0GKpPDxr
#

def get_jump(curr, val, N):
  return (curr + val) % N


def check_loop(arr, N, idx, bad_condition):
  slow = idx
  fast = idx

  while fast is not None:
    if bad_condition(arr[slow]):
      return False
    slow = get_jump(slow, arr[slow], N)

    if bad_condition(arr[fast]):
      return False

    fast_i = get_jump(fast, arr[fast], N)

    if bad_condition(arr[fast_i]):
      return False

    fast = get_jump(fast_i, arr[fast_i], N)

    if bad_condition(arr[fast]):
      return False

    if slow == fast:
      return True

def circular_array_loop_exists(arr):
  N = len(arr)

  for i in range(len(arr)):
    if check_loop(arr=arr, N=N, idx=i, bad_condition=lambda x : x < 0):
      return True
  
  for i in range(len(arr)):
    if check_loop(arr=arr, N=N, idx=i, bad_condition=lambda x : x > 0):
      return True

  return False


def main():
  print(circular_array_loop_exists([1, 2, -1, 2, 2]))
  print(circular_array_loop_exists([2, 2, -1, 2]))
  print(circular_array_loop_exists([2, 1, -1, -2]))


main()
