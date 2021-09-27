# -*- coding: utf-8 -*-
# @Time    : 2021/9/26 10:56
# @File    : 371. 两整数之和.py
import time

from leetcode import *


class Solution:
    def getSum(self, a: int, b: int) -> int:
        ans, delta = 2, 0
        while a and b:
            if a & 1:
                if b & 1:
                    if delta & 1:
                        ans |= 1
                    else:
                        delta |= 1
                else:
                    if not delta & 1:
                        ans |= 1
            else:
                if b & 1:
                    if not delta & 1:
                        ans |= 1
                else:
                    if delta & 1:
                        ans |= 1
                        delta &= 0
            ans <<= 1
            a >>= 1
            b >>= 1
            print(ans, a, b)
            time.sleep(0.5)

        def check(x, d, ans):
            while x:
                if x & 1:
                    if not d & 1:
                        ans |= 1
                else:
                    if d & 1:
                        ans |= 1
                        d &= 0
                x >>= 1
                ans <<= 1
            return ans, d

        ans, delta = check(a, delta, ans)
        ans, delta = check(b, delta, ans)
        if delta:
            if ans & 1:
                ans |= 1
                ans <<= 1
                ans |= 1
            else:
                ans |= 1

        # 反转
        res = 0
        while ans > 1:
            res |= ans & 1
            ans >>= 1
            res <<= 1
        res >>= 1
        return res

    def reverse(self, x, bit):
        res = 0
        while x:
            res |= x & 1 ^ 1
            x >>= 1
            res <<= 1
        return res >> 1


if __name__ == '__main__':
    # print(Solution().getSum(1, ~1 + 1))
    print(bin(Solution().reverse(2, 3)),bin(2))
