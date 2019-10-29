class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def dfs(self, total=0):
        total = (total * 10) + self.val

        if self.left is None and self.right is None:
            return total

        left = 0
        right = 0
        if self.left is not None:
            left = self.left.dfs(total=total)

        if self.right is not None:
            right = self.right.dfs(total=total)

        return left + right


def find_sum_of_path_numbers(root):
    return root.dfs()


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
