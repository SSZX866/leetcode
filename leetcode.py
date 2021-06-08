# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 11:15
# @File    : model.py

# 力扣可以支持到 1e7 的算法复杂度。也就是说数据范围到 50000 的基本是 O(n),到 20000 的是 O(nlogn)
# 到 1000 的是 O(n^2),到 100 的是 O(n^3),到 30 的是 O(n^4),到 20是 O(2^n)

from typing import List
import heapq, math, itertools, functools, bisect
from collections import *
from functools import lru_cache


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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def buildChainWithValue(head):
    if not head: return None
    cur = ListNode(head[0])
    root = cur
    for each in head[1:]:
        p = ListNode(each)
        cur.next = p
        cur = cur.next
    return root


def printChainToValue(root):
    print('[', end='')
    while root:
        if root.next:
            print(root.val, end=', ')
        else:
            print(root.val, end='')
        root = root.next
    print(']', end='')


null = None
true = True
false = False
