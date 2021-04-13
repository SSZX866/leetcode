# -*- coding: utf-8 -*-
# @Time    : 2021/3/29 10:55
# @File    : 237. 删除链表中的节点.py

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next