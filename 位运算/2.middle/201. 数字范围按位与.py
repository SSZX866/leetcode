# -*- coding: utf-8 -*-
# @Time    : 2021/9/4 19:31
# @File    : 201. 数字范围按位与.py
from leetcode import *


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0
        while left != right:
            i += 1
            left >>= 1
            right >>= 1
        return left << i
