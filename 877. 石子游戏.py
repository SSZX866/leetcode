# -*- coding: utf-8 -*-
# @Time    : 2021/6/16 15:58
# @File    : 877. 石子游戏.py
from leetcode import *


# [3,2,10,4]
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        Alex, Li = 0, 0
        for i in range(n):
            if piles[0] > piles[-1]:
                if i % 2:
                    Li += piles.pop(0)
                else:
                    Alex += piles.pop(0)
            else:
                if i % 2:
                    Li += piles.pop(1)
                else:
                    Alex += piles.pop(-1)
        return Alex > Li


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
