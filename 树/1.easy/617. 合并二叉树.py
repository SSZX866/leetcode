# -*- coding: utf-8 -*-
# @Time    : 2021/08/02 12:16
# @File    : 617. 合并二叉树
from leetcode import *


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1: return root2
        if not root2: return root1
        stack2 = [root2]
        stack1 = [root1]
        while stack2:
            if not stack1: break
            node1 = stack1.pop()
            node2 = stack2.pop()
            node2.val += node1.val
            if node1.left and node2.left:
                stack1.append(node1.left)
                stack2.append(node2.left)
            elif node1.left and not node2.left:
                node2.left = node1.left
            if node1.right and node2.right:
                stack1.append(node1.right)
                stack2.append(node2.right)
            elif node1.right and not node2.right:
                node2.right = node1.right
        return root2


class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1

        mergeroot = TreeNode(-1)
        mergeroot.val = root1.val + root2.val
        mergeroot.left = self.mergeTrees(root1.left, root2.left)
        mergeroot.right = self.mergeTrees(root1.right, root2.right)
        return mergeroot


if __name__ == '__main__':
    root1 = buildTreeWithValue([3, 4, 5, 1, 2])
    root2 = buildTreeWithValue([4, 1, 2, 1])
    print(Solution().mergeTrees(root1, root2))
