# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 15:23
# @File    : 1094. 拼车.py
from leetcode import *

# 差分数组
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        delta = [0] * 1001
        for trip in trips:
            delta[trip[1]] += trip[0]
            delta[trip[2]] -= trip[0]
        ans = [delta[0]]
        for i in range(1, 1001):
            if ans[-1] > capacity: return False
            ans.append(ans[-1] + delta[i])
        return True if ans[-1] <= capacity else False
