# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 9:32
# @File    : 1011. 在 D 天内送达包裹的能力.py
from leetcode import *


# 滑动窗口超时
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        pre, n = [0], len(weights)
        for i in range(n):
            pre.append(pre[-1] + weights[i])
        i, ans = 0, max(weights)
        while True:
            i, ship = 1, 1
            for j in range(2, n + 1):
                if pre[j] - pre[i - 1] > ans:
                    ship += 1
                    i = j
            if ship <= D:
                return ans
            ans += 1


# 二分 hi = sum(weights) lo = max(weights)
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        lo = max(weights)
        hi = lo * len(weights) // D
        # hi, lo = sum(weights), max(weights)
        # 将hi改为lo * len(weights) // D可缩短时间，因为对于很长的数据量来说，
        # 虽然增加了搜索范围，但是sum需要遍历整个数组，而二分是折半的效率，因此总体是效率提升的
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.check(mid, weights, D):
                hi = mid
            else:
                lo = mid + 1
        return lo

    # # 贪心使得每天能够装的货物在target以下最大的结果，若最后所有货物都装上则true否则则为false
    # # 由于双层循环，复杂度较高
    # def check(self, target, weights, D):
    #     i, j = 0, 1
    #     for _ in range(D):
    #         tmp = 0
    #         while i < len(weights):
    #             tmp += weights[i]
    #             i += 1
    #             if tmp > target:
    #                 break
    #         if tmp > target:
    #             i -= 1
    #         if i == len(weights):
    #             return True
    #     return i >= len(weights)

    # 直接遍历货物的重量，计算按照target需要多少天来完成，减少一次嵌套循环
    def check(self, target, weights, D):
        d, tmp = 1, 0
        for weight in weights:
            tmp += weight
            if tmp <= target:
                continue
            else:
                d += 1
                tmp = weight
        return d <= D


if __name__ == '__main__':
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    D = 5
    # weights = [1, 2, 3, 1, 1]
    # D = 4
    print(Solution().shipWithinDays(weights, D))
