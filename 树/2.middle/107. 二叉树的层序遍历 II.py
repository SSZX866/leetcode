# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 20:04
# @File    : 107. 二叉树的层序遍历 II.py
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        def dfs(root, deep, ans):
            if not root: return
            if deep > len(ans):
                ans.append([])
            ans[deep - 1].append(root.val)
            dfs(root.left, deep + 1, ans)
            dfs(root.right, deep + 1, ans)

        ans = []
        dfs(root, 1, ans)
        # print(ans)
        return ans[::-1]


if __name__ == '__main__':
    null = None
    root = buildTreeWithValue([3, 9, 20, null, null, 15, 7])
    print(Solution().levelOrderBottom(root))
