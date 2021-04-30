# -*- coding: utf-8 -*-
# @Time    : 2021/4/30 10:07
# @File    : 137. 只出现一次的数字 II.py
import collections

from leetcode import *


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums) - 1, 3):
            a = nums[i]
            b = nums[i + 1]
            c = nums[i + 2]
            if a == b == c: continue
            if a == b:
                return c
            elif b == c:
                return a
            return b
        return nums[-1]

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (3*sum(set(nums)) - sum(nums))//2


if __name__ == '__main__':
    nums = [2, 2, 3, 2]
    nums = [0, 1, 0, 1, 0, 1, 99]
    print(Solution().singleNumber(nums))
