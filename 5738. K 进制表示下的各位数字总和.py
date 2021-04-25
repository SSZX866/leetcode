# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 10:30
# @File    : 5738. K 进制表示下的各位数字总和.py
from leetcode import *
import functools


class Solution:
    def __init__(self):
        self.ans = 0

    def sumBase(self, n: int, k: int) -> int:
        if n // k == 0: return self.ans + n % k
        self.ans += n % k + self.sumBase(n // k, k)
        return self.ans


class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ans = 0
        while n > 0:
            ans += n % k
            n //= k
        return ans


if __name__ == '__main__':
    print(Solution().sumBase(34, 6))
    print(Solution().sumBase(10, 10))
