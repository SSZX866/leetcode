# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 10:35
# @File    : 5746. 到目标元素的最小距离.py
from leetcode import *


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        a = start - 1 - nums[start - 1::-1].index(target) if target in nums[:start] else 10000
        b = start + nums[start:].index(target) if target in nums[start:] else 10000
        return min(abs(a - start), abs(b - start))


if __name__ == '__main__':
    nums = [5, 3, 6]
    target = 5
    start = 2
    print(Solution().getMinDistance(nums, target, start))
