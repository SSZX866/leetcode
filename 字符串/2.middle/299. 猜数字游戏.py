# -*- coding: utf-8 -*-
# @Time:    2021/11/8 10:46
# @File:    299. 猜数字游戏.py
from leetcode import *


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        A = 0
        nums = [[0] * 10 for _ in range(2)]
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                nums[0][int(secret[i])] += 1
                nums[1][int(guess[i])] += 1
        B = 0
        for i in range(10):
            B += min(nums[0][i], nums[1][i])
        return str(A) + 'A' + str(B) + 'B'
