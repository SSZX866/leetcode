# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 20:47
# @File    : 103. 二叉树的锯齿形层序遍历.py
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        cur_layer = [root]

        ans = []
        while cur_layer:
            next_layer = []
            cur_val = []
            for cur in cur_layer:
                cur_val.append(cur.val)
                if cur.left: next_layer.append(cur.left)
                if cur.right: next_layer.append(cur.right)
            ans.append(cur_val)
            cur_layer = next_layer
        return [a[::-1] if i % 2 else a for i, a in enumerate(ans)]