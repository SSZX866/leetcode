# -*- coding: utf-8 -*-
# @Time    : 2021/07/27 10:08
# @File    : 671. 二叉树中第二小的节点
from leetcode import *


# 维护容量为二的大顶堆，比堆顶小的入堆，排除重复的
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root: return -1
        heap = []
        stack = [root]
        while stack:
            node = stack.pop()
            if -node.val not in heap:
                if len(heap) < 2:
                    heapq.heappush(heap, -node.val)
                elif -heap[0] > node.val:
                    heapq.heappop(heap)
                    heapq.heappush(heap, -node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        return -heap[0] if len(heap) == 2 else -1
