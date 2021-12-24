# -*- coding: utf-8 -*-
# @Time    : 2021/12/21 10:17
# @File    : 1154. 一年中的第几天.py
from leetcode import *


class Solution:
    def dayOfYear(self, date: str) -> int:
        tmp = {1, 3, 5, 7, 8, 10, 12}
        dic = {k: 31 if k in tmp else 30 for k in range(1, 13)}
        year, month, day = map(int, date.split('-'))
        dic[2] = 29 if (year % 100 and not year % 4) or not year % 400 else 28
        res = day
        for m in range(1, month): res += dic[m]
        return res
