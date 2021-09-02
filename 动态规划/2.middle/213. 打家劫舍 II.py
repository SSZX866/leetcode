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
        # 选第一个不选最后一个
        for i in range(2, n - 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        ans = dp[-2]

        # 不选第一个选最后一个
        nums = nums[1:]
        dp[0] = nums[0]
        if n == 1: return dp[0]
        dp[1] = max(nums[:2])
        for i in range(2, n - 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        ans = max(ans, dp[-2])
        return ans


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        dp = [[0] * 2 for _ in nums]

        dp[0][1] = nums[0]
        for i in range(1, len(nums) - 1):
            dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])
            dp[i][1] = dp[i - 1][0] + nums[i]
        ans = max(dp[-2])

        dp[1][1] = nums[1]
        dp[1][0] = 0
        for i in range(2, len(nums)):
            dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])
            dp[i][1] = dp[i - 1][0] + nums[i]

        ans = max(ans, max(dp[-1]))
        return ans


class Solution:
    def rob(self, nums: List[int]) -> int:
        def func(ns):
            pre = [[0] * 2 for _ in ns]
            pre[0][1] = ns[0]
            for i in range(1, len(ns)):
                pre[i][0] = max(pre[i - 1][1], pre[i - 1][0])
                pre[i][1] = pre[i - 1][0] + ns[i]
            return max(pre[-1])

        return max(func(nums[1:]), func(nums[:-1])) if len(nums) != 1 else nums[0]


if __name__ == '__main__':
    nums = [2, 3, 2]
    nums = [1, 2, 3, 1]
    nums = [0]
    nums = [1, 3, 5, 7, 8, 1, 4, 5]
    print(Solution().rob(nums))
