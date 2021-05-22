# -*- coding: utf-8 -*-
# @Time    : 2021/5/22 10:33
# @File    : 810. 黑板异或游戏.py
from leetcode import *


class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        return len(nums) % 2 == 0 or functools.reduce(lambda x, y: x ^ y, nums) == 0

if __name__ == '__main__':
    nums = [1, 1, 2]
    nums = [0, 1]
    nums = [1, 1, 2, 3]
    print(Solution().xorGame(nums))
