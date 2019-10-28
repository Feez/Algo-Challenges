from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  result = []
  
  q = deque([root])

  while q:
    level_size = len(q)
    result.append(list())

    for i in range(level_size):
      curr = q.popleft()

      if curr.left is not None:
        q.append(curr.left)

      if curr.right is not None:
        q.append(curr.right)
      
      result[-1].append(curr.val)
    
  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))


main()
