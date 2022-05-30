# -*- coding: utf-8 -*-
# @Time    : 2021/11/29 09:24
# @File    : 519. 随机翻转矩阵.py
from leetcode import *


class Solution:
    def __init__(self, m: int, n: int):
        self.m, self.n = m, n
        self.total = m * n - 1
        self.record = dict()

    def flip(self) -> List[int]:
        r = random.randint(0, self.total)
        idx = self.record.get(r, r)
        # 相当于total的值没被用，将那个值填入idx位置；
        # 被用了的话，将它那里填入的没被用的值填入
        self.record[r] = self.record.get(self.total, self.total)
        self.total -= 1
        ans = [idx // self.n, idx % self.n]
        return ans

    def reset(self) -> None:
        self.total = self.m * self.n - 1
        self.record = dict()

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
