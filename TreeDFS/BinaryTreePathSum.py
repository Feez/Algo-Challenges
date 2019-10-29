class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def dfs(self, goal):
    curr = goal - self.val
    if curr == 0:
      return True

    if self.left is not None:
      if self.left.dfs(curr):
        return True
    
    if self.right is not None:
      if self.right.dfs(curr):
        return True

    return False

def has_path(root, total):
  return root.dfs(goal=total)


def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has path: " + str(has_path(root, 23)))
  print("Tree has path: " + str(has_path(root, 16)))


main()
