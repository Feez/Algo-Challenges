from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_minimum_depth(root):
  q = deque([root])
  curr_level = 1

  while q:
    level_size = len(q)

    for i in range(level_size):
      curr = q.popleft()

      if curr.left is None and curr.right is None:
        return curr_level

      if curr.left is not None:
        q.append(curr.left)

      if curr.right is not None:
        q.append(curr.right)

    curr_level += 1


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
