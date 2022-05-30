# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 09:49
# @File    : 29. 两数相除.py
from leetcode import *


# 二分+移位乘法
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0: return 0
        mark = True if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0) else False
        dividend, divisor = abs(dividend), abs(divisor)
        if dividend < divisor: return 0
        lo, hi = 0, dividend + 1
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            res = self.calc(mid, divisor)
            if res > dividend:
                hi = mid
            elif res < dividend:
                lo = mid + 1
            else:
                lo = mid + 1
                break
        ans = lo - 1 if not mark else -lo + 1
        ans = 2147483647 if ans > 2147483647 else ans
        ans = -2147483648 if ans < -2147483648 else ans
        return ans

    # def calc(self, a, b):
    #     if a < b: return self.calc(b, a)
    #     ans = 0
    #     for i in range(b):
    #         ans += a
    #     return ans

    # 移位乘法
    # def calc(self, a, b):
    #     if a < b: return self.calc(b, a)
    #     ans = 0
    #     binary = bin(b)[2:]
    #     for i in range(len(binary)):
    #         if binary[i] == '1':
    #             ans += a << (len(binary) - i - 1)
    #     return ans

    # 移位乘法
    #   123 *  23
    # = 123 * (16 + 4 + 2 + 1)
    # = 123 * 16 + 123 * 4 + 123 * 2 + 123 * 1
    # = 123 << 4 + 123 << 2 + 123 << 1 + 123 << 0
    def calc(self, a, b):
        if a < b: return self.calc(b, a)
        ans, index = 0, 0
        while b:
            if b & 1:
                ans += a << index
            index += 1
            b >>= 1
        return ans