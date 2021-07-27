# -*- coding: utf-8 -*-
# @Time    : 2021/07/27 10:42
# @File    : 977. 有序数组的平方
from leetcode import *


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        negative = -1
        for i, num in enumerate(nums):
            if num < 0:
                negative = i
            else:
                break

        ans = list()
        i, j = negative, negative + 1
        while i >= 0 or j < n:
            if i < 0:
                ans.append(nums[j] * nums[j])
                j += 1
            elif j == n:
                ans.append(nums[i] * nums[i])
                i -= 1
            elif nums[i] * nums[i] < nums[j] * nums[j]:
                ans.append(nums[i] * nums[i])
                i -= 1
            else:
                ans.append(nums[j] * nums[j])
                j += 1

        return ans
