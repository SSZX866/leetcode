# -*- coding: utf-8 -*-
# @Time    : 2021/12/17 09:50
# @File    : 1518. 换酒问题.py
from leetcode import *


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            exchange = numBottles // numExchange
            numBottles %= numExchange
            numBottles += exchange
            res += exchange
        return res
