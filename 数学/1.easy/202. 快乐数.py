# -*- coding: utf-8 -*-
# @Time    : 2021/9/5 20:59
# @File    : 202. 快乐数.py
from leetcode import *


# 出现死循环的情况 -> 得到的新数之前得到过 -> set记录
class Solution:
    def isHappy(self, n: int) -> bool:
        dic = {n}
        while n != 1:
            tmp = 0
            while n:
                tmp += (n % 10) ** 2
                n //= 10
            if tmp in dic: return False
            dic.add(tmp)
            n = tmp
        return True
