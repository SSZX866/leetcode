# -*- coding: utf-8 -*-
# @Time    : 2021/4/22 16:28
# @File    : 23. 合并K个升序链表.py
from leetcode import *


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        res = []
        for node in lists:
            while node:
                res.append((node.val,node))
                # heapq.heappush(res, (node.val, id(node), node))
                node = node.next
        res.sort(key=lambda x:x[0])
        node = dummy = ListNode()
        while res:
            node.next = res.pop(0)[1]
            node = node.next
        return dummy.next


if __name__ == '__main__':
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    lists = [[],[-2,-1,-1]]
    lists = [buildChainWithValue(node) for node in lists]
    printChainToValue(Solution().mergeKLists(lists))
