# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 15:30
# @File    : 1109. 航班预订统计.py
from leetcode import *


# 差分数组
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        delta = [0] * (n + 2)
        for booking in bookings:
            delta[booking[0]] += booking[2]
            delta[booking[1] + 1] -= booking[2]
        ans = [0]
        for i in range(n + 1):
            ans.append(ans[-1] + delta[i])
        return ans[2:]
