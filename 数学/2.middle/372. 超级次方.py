# -*- coding: utf-8 -*-
# @Time    : 2021/12/5 11:15
# @File    : 372. 超级次方.py
from leetcode import *


# 递归快速幂
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        def quickPower(e, n):
            if n % 2: return quickPower(e, n - 1) * e % 1337
            if n != 0: return (quickPower(e, n // 2) % 1337) ** 2 % 1337
            return 1

        n = reduce(lambda x, y: x * 10 + y, b)
        return quickPower(a, n)


# 非递归
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        n = reduce(lambda x, y: x * 10 + y, b)
        ans = 1
        while n:
            if n & 1: ans = a * ans % 1337
            a = (a ** 2) % 1337
            n >>= 1

        return ans
