# -*- coding: utf-8 -*-
# @Time    : 2021/9/18 13:46
# @File    : 292. Nim 游戏.py
from leetcode import *


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
