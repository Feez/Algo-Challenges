from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = deque()

  q = deque([root])
  direction = 0
  
  while q:
    level_size = len(q)
    
    level = deque()

    for i in range(level_size):
      curr = q.popleft()

      if direction == 0:
        level.append(curr.val)
      else:
        level.appendleft(curr.val)

      if curr.left is not None:
        q.append(curr.left)

      if curr.right is not None:
        q.append(curr.right)

    direction = (direction + 1) % 2

    result.append(list(level))

  return list(result)


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))


main()
