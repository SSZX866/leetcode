# -*- coding: utf-8 -*-
# @Time    : 2021/5/23 10:36
# @File    : 5764. 准时到达的列车最小时速.py
from leetcode import *


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) - 1 > hour: return -1

        def check(target):
            cur_time = 0
            for i in range(len(dist)):
                cur_time += math.ceil(dist[i] / target) if i != len(dist) - 1 else dist[i] / target
            return cur_time <= hour

        lo, hi = 1, 10000000
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if not check(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo


if __name__ == '__main__':
    dist = [1, 3, 2]
    hour = 2.7
    dist = [1, 3, 2]
    hour = 6
    dist = [1,1,100000]
    hour = 2.01
    print(Solution().minSpeedOnTime(dist, hour))
