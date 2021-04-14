# -*- coding: utf-8 -*-
# @Time    : 2021/4/14 15:23
# @File    : 199. 二叉树的右视图.py
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
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        cur_layer, ans = [root], []
        while cur_layer:
            ans.append([])
            next_layer = []
            for node in cur_layer:
                ans[-1].append(node.val)
                if node.left: next_layer.append(node.left)
                if node.right: next_layer.append(node.right)
            cur_layer = next_layer
        return [x[-1] for x in ans]


if __name__ == '__main__':
    null = None
    root = [1, 2, 3, null, 5, null, 4]
    root = buildTreeWithValue(root)
    print(Solution().rightSideView(root))
