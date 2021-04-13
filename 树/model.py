# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 11:12
# @File    : model.py
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


def printTreeToValue(root):
    print('[', end='')
    if root:
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            if queue:
                print(node.val, end=', ')
            else:
                print(node.val, end='')
    print(']', end='')

# printTreeToValue(buildTreeWithValue([1,3,5,None,1]))
