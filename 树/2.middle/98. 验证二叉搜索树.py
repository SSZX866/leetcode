# -*- coding: utf-8 -*-
# @Time    : 2021/6/22 16:44
# @File    : 98. 验证二叉搜索树.py
from leetcode import *


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root: return True
        stack = [[root, False]]
        pre_val = None
        while stack:
            node, visit = stack.pop()
            if visit:
                # if pre_val and node.val <= pre_val: return False
                if pre_val is not None and node.val <= pre_val: return False
                pre_val = node.val
            else:
                if node.right: stack.append([node.right, False])
                stack.append([node, True])
                if node.left: stack.append([node.left, False])
        return True


if __name__ == '__main__':
    root = buildTreeWithValue([2, 1, 3])
    root = buildTreeWithValue([0, null, -1])
    print(Solution().isValidBST(root))
