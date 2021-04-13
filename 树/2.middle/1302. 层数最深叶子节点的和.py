# -*- coding: utf-8 -*-
# @Time    : 2021/4/1 19:02
# @File    : 1302. 层数最深叶子节点的和.py

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 层次遍历解法
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root: return 0
        queue, res, stack, layer = [[root,0]], 0, [[root,0]], 0
        # [38, 43, 70, 16, null, 78, 91, null, 71, 27, null, 71, null, null, null, 71]这种情况不行
        # queue, res, stack = [root], 0, [root]
        # while queue:
        #     node = queue.pop(0)
        #     if node.left:
        #         queue.append(node.left)
        #         stack.append(node.left)
        #     if node.right:
        #         queue.append(node.right)
        #         stack.append(node.right)
        # while stack and not (stack[-1].left or stack[-1].right):
        #     res += stack.pop().val
        while queue:
            layer = queue[0][1] + 1
            node = queue.pop(0)[0]
            if node.left:
                queue.append([node.left,layer])
                stack.append([node.left,layer])
            if node.right:
                queue.append([node.right,layer])
                stack.append([node.right,layer])
        while stack and (stack[-1][1] == layer - 1):
            res += stack.pop()[0].val
        return res

# dfs解法
class Solution:
    def __init__(self):
        self.maxdep = -1
        self.total = 0

    def deepestLeavesSum(self, root: TreeNode) -> int:
        def dfs(node, dep):
            if not node:
                return
            if dep > self.maxdep:
                self.maxdep, self.total = dep, node.val
            elif dep == self.maxdep:
                self.total += node.val
            dfs(node.left, dep + 1)
            dfs(node.right, dep + 1)

        dfs(root, 0)
        return self.total