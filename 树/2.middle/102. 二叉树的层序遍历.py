# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 20:30
# @File    : 102. 二叉树的层序遍历.py
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTreeWithValue(root):
    if not root: return root
    tree = TreeNode(root[0])
    queue = [tree]
    i = 1
    while i < len(root):
        node = queue.pop(0)
        if root[i] == None:
            i += 1
            if i < len(root) and root[i] != None:
                node.right = TreeNode(root[i])
                queue.append(node.right)
            i += 1
        else:
            node.left = TreeNode(root[i])
            queue.append(node.left)
            i += 1
            if i < len(root) and root[i] != None:
                node.right = TreeNode(root[i])
                queue.append(node.right)
            i += 1
    return tree


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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
        return ans


if __name__ == '__main__':
    null = None
    root = buildTreeWithValue([3, 9, 20, null, null, 15, 7])
    print(Solution().levelOrder(root))
