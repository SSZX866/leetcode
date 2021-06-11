# -*- coding: utf-8 -*-
# @Time    : 2021/6/11 11:21
# @File    : 279. 完全平方数.py
from leetcode import *


# 贪心 不对
class Solution:
    def __init__(self):
        self.help = [i ** 2 for i in range(1, 100)]

    @lru_cache(None)
    def numSquares(self, n: int) -> int:
        print(n)
        if n == 0: return 0
        index = bisect.bisect(self.help, n)
        if self.help[index] == n:
            return 0
        return self.numSquares(n - self.help[index - 1]) + 1


# 数学定理 任何一个正整数都可以表示成不超过四个整数的平方之和。 推论：满足四数平方和定理的数n（四个整数的情况），必定满足 n=4^a(8b+7)
class Solution:
    def numSquares(self, n: int) -> int:
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        a = 0
        while a ** 2 <= n:
            b = int((n - a ** 2) ** 0.5)
            if a ** 2 + b ** 2 == n:
                return (not not a) + (not not b)
            a += 1
        return 3


# 背包

if __name__ == '__main__':
    print(Solution().numSquares(12))
