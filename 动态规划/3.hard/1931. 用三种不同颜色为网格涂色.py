# -*- coding: utf-8 -*-
# @Time    : 2021/7/11 11:24
# @File    : 5811. 用三种不同颜色为网格涂色.py
from leetcode import *


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10 ** 9 + 7
        fi0, fi1 = 0,6
        for i in range(2, n + 1):
            fi0, fi1 = (2 * fi0 + 2 * fi1) % mod, (2 * fi0 + 3 * fi1) % mod
        return (fi0 + fi1) % mod

if __name__ == '__main__':
    m = 2
    n = 1
    print(Solution().colorTheGrid(1,2))