# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 20:11
# @File    : LCP 01. 猜数字.py
from leetcode import *


class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        return [x == y for x, y in zip(guess, answer)].count(True)


if __name__ == '__main__':
    guess = [1, 2, 3]
    answer = [3, 4, 1]
    print(Solution().game(guess, answer))
