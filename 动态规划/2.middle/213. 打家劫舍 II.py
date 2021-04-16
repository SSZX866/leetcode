# -*- coding: utf-8 -*-
# @Time    : 2021/4/15 09:42
# @File    : 213. 打家劫舍 II.py
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        if n == 1: return dp[0]
        dp[1] = max(nums[:2])
        #选第一个不选最后一个
        for i in range(2, n-1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        ans = dp[-2]

        #不选第一个选最后一个
        nums = nums[1:]
        dp[0] = nums[0]
        if n == 1: return dp[0]
        dp[1] = max(nums[:2])
        for i in range(2, n - 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        ans = max(ans, dp[-2])
        return ans

if __name__ == '__main__':
    nums = [2, 3, 2]
    nums = [1, 2, 3, 1]
    nums = [0]
    nums = [1,3,5,7,8,1,4,5]
    print(Solution().rob(nums))
