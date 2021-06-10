# -*- coding: utf-8 -*-
# @Time    : 2021/6/9 14:51
# @File    : 剑指 Offer 54. 二叉搜索树的第k大节点.py
import heapq

from leetcode import *


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        heap = []

        def preOrder(node):
            if not node: return
            if len(heap) < k:
                heapq.heappush(heap, node.val)
            else:
                if heap[0] < node.val:
                    heapq.heappushpop(heap, node.val)
            preOrder(node.left)
            preOrder(node.right)

        preOrder(root)
        return heap[0]
