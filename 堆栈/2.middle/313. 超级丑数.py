# -*- coding: utf-8 -*-
# @Time    : 2021/4/20 16:34
# @File    : 313. 超级丑数.py
from leetcode import *
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = []
        