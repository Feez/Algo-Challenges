class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def dfs(self, sequence, depth=0):
        if depth >= len(sequence):
            return False

        if sequence[depth] == self.val:
            if depth == len(sequence) - 1:
                return True

            if self.left is not None:
                if self.left.dfs(sequence=sequence, depth=depth + 1):
                    return True

            if self.right is not None:
                if self.right.dfs(sequence=sequence, depth=depth + 1):
                    return True
        
        return False

def find_path(root, sequence):
    return root.dfs(sequence=sequence)


def main():

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
