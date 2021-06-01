# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 10:44
# @File    : 1744. 你能在你最喜欢的那天吃到你最喜欢的糖果吗？.py
from leetcode import *


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        ans, pre = [], [0]
        for candy in candiesCount:
            pre.append(pre[-1] + candy)
        for query in queries:
            hi = (1 + query[1]) * query[2]
            lo = query[1]
            print(lo, hi, pre[query[0] + 1], pre[query[0]])
            if lo >= pre[query[0] + 1] or hi <= pre[query[0]]:
                ans.append(False)
            else:
                ans.append(True)
        return ans


if __name__ == '__main__':
    candiesCount = [5, 2, 6, 4, 1]
    queries = [[1, 3, 1]]

    # print(queries[
    #           len(
    #               [false, false, false, false, true, false, false, false, false, false, false, true, true, false, true,
    #                true, true, true, false, false, false, false, true, false])])
    print(Solution().canEat(candiesCount, queries))
