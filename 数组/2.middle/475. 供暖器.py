# -*- coding: utf-8 -*-
# @Time    : 2021/12/20 10:13
# @File    : 475. 供暖器.py
from leetcode import *


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        n = len(heaters)

        def findNeighbor(target):
            lo, hi = 0, n
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if heaters[mid] < target:
                    lo = mid + 1
                elif heaters[mid] > target:
                    hi = mid
                else:
                    return mid
            return lo

        res = 0
        for house in houses:
            idx = findNeighbor(house)
            if idx == n:
                tmp = abs(heaters[idx - 1] - house)
            elif heaters[idx] == house:
                continue
            else:
                tmp = min(abs(heaters[idx] - house), abs(heaters[idx - 1] - house))
            res = max(tmp, res)
        return res
