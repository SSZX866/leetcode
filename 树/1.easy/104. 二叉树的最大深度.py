class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return max(self.maxDepth(root.right), self.maxDepth(root.left)) + 1

if __name__ == '__main__':
    root = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
    print(Solution().maxDepth(root))
