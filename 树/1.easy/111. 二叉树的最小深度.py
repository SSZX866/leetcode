class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if root.right and not root.left:
            return self.minDepth(root.right)+1
        if root.left and not root.right:
            return self.minDepth(root.left)+1
        else:
            return min(self.minDepth(root.left),self.minDepth(root.right))+1