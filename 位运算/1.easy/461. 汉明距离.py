# -*- coding: utf-8 -*-
# @Time    : 2021/4/29 20:34
# @File    : 461. 汉明距离.py
from leetcode import *


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = x ^ y
        ans = 0
        for i in range(32):
            if a & 1 == 1:
                ans += 1
            a = a >> 1
        return ans


if __name__ == '__main__':
    x = 1
    y = 4
    print(Solution().hammingDistance(x, y))
