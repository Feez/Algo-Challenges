class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def dfs(self, goal, all_paths, curr_path=None):
        if curr_path is None:
            curr_path = []

        curr_path.append(self.val)
        curr_val = goal - self.val

        if curr_val == 0:
            all_paths.append(curr_path)

        if self.left is not None:
            self.left.dfs(goal=curr_val, all_paths=all_paths, curr_path=list(curr_path))
        
        if self.right is not None:
            self.right.dfs(goal=curr_val, all_paths=all_paths, curr_path=list(curr_path))

        return all_paths


def find_paths(root, total):
    return root.dfs(goal=total, all_paths=[])


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
          ": " + str(find_paths(root, sum)))


main()
