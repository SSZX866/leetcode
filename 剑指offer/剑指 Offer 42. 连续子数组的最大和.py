# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 11:03
# @File    : 剑指 Offer 42. 连续子数组的最大和.py
from leetcode import *


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tmp = ans = 0
        for i in range(len(nums)):
            tmp = max(tmp + nums[i], nums[i])
            ans = max(tmp, ans)
        return ans if ans != 0 else max(nums)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]
        for num in nums:
            dp.append(dp[-1] + num)
        ans = nums[0]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                ans = max(ans, dp[j] - dp[i])
        return ans


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums = [-1]
    # nums = [1,2]
    print(Solution().maxSubArray(nums))
