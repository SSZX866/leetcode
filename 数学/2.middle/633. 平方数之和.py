# -*- coding: utf-8 -*-
# @Time    : 2021/4/28 16:22
# @File    : 633. 平方数之和.py
from leetcode import *
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        dic = set()
        for i in range(math.ceil(math.sqrt(c))+1):
            tmp = i * i
            if tmp in dic: return True
            dic.add(c - tmp)
        for i in range(math.ceil(math.sqrt(c))+1):
            tmp = i * i
            if tmp in dic: return True
        return False


if __name__ == '__main__':
    c = 2
    print(Solution().judgeSquareSum(c))
