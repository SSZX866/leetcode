# -*- coding: utf-8 -*-
# @Time    : 2021/5/10 20:35
# @File    : 1482. 制作 m 束花所需的最少天数.py
from leetcode import *


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k: return -1
        lo, hi = min(bloomDay), max(bloomDay)

        def check(day):
            flowerContinuation = bouquet = 0
            for bloom in bloomDay:
                if bloom <= day:
                    flowerContinuation += 1
                    if flowerContinuation == k:
                        bouquet += 1
                        flowerContinuation = 0
                        if bouquet == m:
                            return True
                else:
                    flowerContinuation = 0
            return False

        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == '__main__':
    bloomDay, m, k = [1, 10, 3, 10, 2], 3, 1
    bloomDay, m, k = [7, 7, 7, 7, 12, 7, 7], 2, 3
    bloomDay, m, k = [1000000000, 1000000000], 1, 1
    print(Solution().minDays(bloomDay, m, k))
