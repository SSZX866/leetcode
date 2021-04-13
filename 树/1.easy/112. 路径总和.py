class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# dfs 回溯解法
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def dfs(path, node, targetSum):
            print(path)
            if node:
                if not node.left and not node.right:
                    if sum(path) + node.val == targetSum:
                        return True
                else:
                    path.append(node.val)
                    if dfs(path, node.left, targetSum): return True
                    path.pop()
                    path.append(node.val)
                    if dfs(path, node.right, targetSum): return True
                    path.pop()
            else:
                return

        if dfs([], root, targetSum): return True
        return False


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        val = 0
        ans = False

        def calc(root, ans, val):
            if not root:
                return ans
            if not root.left and not root.right:
                val += root.val
                if val == targetSum:
                    ans = True
                val = 0
                return ans
            val += root.val
            ans = calc(root.left, ans, val)
            ans = calc(root.right, ans, val)
            return ans

        return calc(root, ans, val)
