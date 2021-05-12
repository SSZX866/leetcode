# -*- coding: utf-8 -*-
# @Time    : 2021/5/12 09:52
# @File    : 1310. 子数组异或查询.py
from leetcode import *


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ans, pre = [], [0]
        for num in arr:
            pre.append(pre[-1] ^ num)
        for query in queries:
            ans.append(pre[query[1] + 1] ^ pre[query[0]])
        return ans


if __name__ == '__main__':
    arr, queries = [1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]]
    print(Solution().xorQueries(arr, queries))
