# -*- coding: utf-8 -*-
# @Time    : 2021/3/29 10:04
# @File    : 771. 宝石与石头.py

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
        for jewel in jewels:
            cnt += stones.count(jewel)
        return cnt