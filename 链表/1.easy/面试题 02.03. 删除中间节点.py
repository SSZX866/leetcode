# -*- coding: utf-8 -*-
# @Time    : 2021/4/23 22:42
# @File    : 面试题 02.03. 删除中间节点.py
from leetcode import *


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
