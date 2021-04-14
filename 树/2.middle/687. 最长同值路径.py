# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 22:58
# @File    : 687. 最长同值路径.py
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
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0

        def help(root):
            if not root: return 0
            left, right = help(root.left), help(root.right)
            leftAndRoot = left + 1 if root.left and root.left.val == root.val else 0
            rightAndRoot = right + 1 if root.right and root.right.val == root.val else 0
            self.ans = max(self.ans, leftAndRoot + rightAndRoot)
            return max(leftAndRoot, rightAndRoot)

        help(root)
        return self.ans


if __name__ == '__main__':
    root = [5, 4, 5, 1, 1, 5]
    print(Solution().longestUnivaluePath(buildTreeWithValue(root)))
