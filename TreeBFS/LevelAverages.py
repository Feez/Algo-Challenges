from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_level_averages(root):
  result = []
  
  q = deque([root])

  while q:
    level_size = len(q)

    total = 0

    for i in range(level_size):
      curr = q.popleft()

      total += curr.val

      if curr.left is not None:
        q.append(curr.left)

      if curr.right is not None:
        q.append(curr.right)


    result.append(total / level_size)
      
  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level averages are: " + str(find_level_averages(root)))


main()
