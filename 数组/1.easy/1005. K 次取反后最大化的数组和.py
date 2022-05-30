# -*- coding: utf-8 -*-
# @Time    : 2021/12/3 09:33
# @File    : 1005. K 次取反后最大化的数组和.py
from leetcode import *


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        zero, ans, minAbs = False, 0, 100
        for i in range(len(nums)):
            if nums[i] < 0:
                minAbs = min(minAbs, -nums[i])
                if k:
                    ans += -nums[i]
                    k -= 1
                else:
                    return ans + sum(nums[i:])
            elif nums[i] == 0:
                zero = True
            else:
                if zero or k % 2 != 1:
                    return ans + sum(nums[i:])
                ans += sum(nums[i + 1:])
                return ans + -nums[i] if nums[i] < minAbs else ans + nums[i] - 2 * minAbs
        if k % 2: ans -= 2 * minAbs
        return ans
