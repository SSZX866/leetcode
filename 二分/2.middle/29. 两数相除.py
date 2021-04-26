# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 20:13
# @File    : 29. 两数相除.py
from leetcode import *


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        mark = False
        if divisor < 0:
            mark = True
            divisor = -divisor
        # if dividend < divisor: return 0
        lo, hi = divisor, dividend
        while lo < hi:
            mid = lo + ((hi - lo) >> 1)
            if self.mul(mid, divisor) > dividend:
                hi = mid
            else:
                lo = mid + 1

        return 1 - lo if mark else lo - 1

    def mul(self, a, b):
        if not (a and b): return 0
        ans, mark = 0, False
        if b < 0:
            mark = True  # 是否为负数
            b = -b
        while b:
            ans += a
            b -= 1

        return -ans if mark else ans


if __name__ == '__main__':
    print(Solution().divide(10, -3))
