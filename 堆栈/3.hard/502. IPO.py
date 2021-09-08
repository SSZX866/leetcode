# -*- coding: utf-8 -*-
# @Time    : 2021/9/8 09:59
# @File    : 502. IPO.py
from leetcode import *


# n^2logn
class HeapNode:
    def __init__(self):
        self.val = []
        self.next = None


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        dummy = HeapNode()
        dummy.next = HeapNode()
        for i in range(len(profits)):
            heapq.heappush(dummy.next.val, (-profits[i], capital[i]))
        while k:
            cur = dummy
            flag = False
            while not flag and cur.next:
                tmp = HeapNode()
                while cur.next.val:
                    profit, cap = heapq.heappop(cur.next.val)
                    if cap > w:
                        heapq.heappush(tmp.val, (profit, cap))
                    else:
                        k -= 1
                        w += -profit
                        flag = not flag
                        # 如果当前节点已空则删除当前节点
                        tmp.next = cur.next if cur.next.val else cur.next.next
                        cur.next = tmp
                        break
                if not flag:
                    # 如果该块未完成则当前节点一定已空
                    tmp.next = cur.next.next
                    cur.next = tmp
                    cur = cur.next
            if not flag: break
        return w


# heap中只存可以启动的项目（即capital<w）每次项目结束后更新heap
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        prof = sorted(zip(profits, capital), key=lambda x: x[1])
        heap = []
        idx, n = 0, len(profits)
        while k:
            while idx < n and prof[idx][1] <= w:
                profit, cap = prof[idx]
                heapq.heappush(heap, (-profit, cap))
                idx += 1
            if heap:
                w += -heapq.heappop(heap)[0]
                k -= 1
            else:
                break
        return w


if __name__ == '__main__':
    k = 2
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 1]
    print(Solution().findMaximizedCapital(k, w, profits, capital))
