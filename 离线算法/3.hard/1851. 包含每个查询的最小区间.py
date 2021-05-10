# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 11:16
# @File    : 5748. 包含每个查询的最小区间.py
from leetcode import *


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals = [interval + [interval[1] - interval[0]] for interval in intervals]
        intervals.sort(key=lambda x: (x[2], x[0]))
        ans = []

        def check(q, mid):
            if intervals[mid][0] <= q <= intervals[mid][1]:
                return True
            return False

        print(intervals)
        for querie in queries:
            lo, hi = 0, len(intervals)
            while lo < hi:

                mid = lo + (hi - lo) // 2
                print(lo, hi, mid, querie)
                if check(querie, mid):
                    hi = mid
                else:
                    lo = mid + 1
            print(lo,mid)
            ans.append(intervals[lo][2]+1)
        return ans


if __name__ == '__main__':
    intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
    queries = [2, 3, 4, 5]
    intervals = [[2, 3], [2, 5], [1, 8], [20, 25]]
    queries = [2, 19, 5, 22]
    print(Solution().minInterval(intervals, queries))
