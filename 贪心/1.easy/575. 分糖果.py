# -*- coding: utf-8 -*-
# @Time    : 2021/11/1 09:08
# @File    : 575. 分糖果.py
from leetcode import *
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType) // 2)