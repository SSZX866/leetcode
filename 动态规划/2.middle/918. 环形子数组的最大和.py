# -*- coding: utf-8 -*-
# @Time    : 2021/07/30 19:57
# @File    : 918. 环形子数组的最大和
from leetcode import *


# 分两种情况，一种为没有跨越边界的情况，一种为跨越边界的情况
# 没有跨越边界的情况直接求子数组的最大和即可；
# 跨越边界的情况可以对数组求和再减去无环的子数组的最小和，即可得到跨越边界情况下的子数组最大和；
# 求以上两种情况的大值即为结果，另外需要考虑全部为负数的情况

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for i in range(1, len(nums)):
            dp.append(max(0, dp[-1]) + nums[i])
        ans = max(dp)
        dp = [nums[0]]
        for i in range(1, len(nums)):
            dp.append(min(0, dp[-1]) + nums[i])
        tmp = sum(nums) - min(dp)
        # 判断是否全为负数（即最小值全选的情况）
        if tmp != 0:
            ans = max(tmp, ans)
        return ans
