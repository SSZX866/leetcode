# -*- coding: utf-8 -*-
# @Time    : 2021/7/10 22:36
# @File    : 5792. 统计平方和三元组的数目.py
from leetcode import *


class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        visit = set()
        for i in range(1, n + 1):
            for j in range(i - 1, n + 1):
                for k in range(j - 1, n + 1):
                    if i * i + j * j == k * k and str(i) + str(j) + str(k) not in visit:
                        ans += 1
                        visit.add(str(i) + str(j) + str(k))
        return ans


class Solution:
    def countTriples(self, n: int) -> int:
        square = {i * i for i in range(1, n + 1)}
        ans = 0
        for i in range(1, n):
            for j in range(1, i):
                if i * i + j * j in square:
                    ans += 2
        return ans
