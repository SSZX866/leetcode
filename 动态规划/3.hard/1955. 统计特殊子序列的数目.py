# -*- coding: utf-8 -*-
# @Time    : 2021/08/02 21:01
# @File    : 1955. 统计特殊子序列的数目
from leetcode import *


# class Solution:
#     def countSpecialSubsequences(self, nums: List[int]) -> int:
#         dp = [[0] * 3 for _ in nums]
#         if nums[0] == 0: dp[0][0] = 1
#         for i in range(1, len(nums)):
#             if nums[i] == 0:
#                 dp[i][0] = dp[i - 1][0] * 2 + 1
#                 dp[i][1] = dp[i - 1][1]
#                 dp[i][2] = dp[i - 1][2]
#             elif nums[i] == 1:
#                 dp[i][0] = dp[i - 1][0]
#                 dp[i][1] = dp[i - 1][0] + dp[i - 1][1] * 2
#                 dp[i][2] = dp[i - 1][2]
#             else:
#                 dp[i][0] = dp[i - 1][0]
#                 dp[i][1] = dp[i - 1][1]
#                 dp[i][2] = dp[i - 1][1] + dp[i - 1][2] * 2
#         return dp[-1][2] % 1000000007


class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        MOD = 1000000007
        dp = [0] * 3
        if nums[0] == 0: dp[0] = 1
        for i in range(1, len(nums)):
            if nums[i] == 0:
                dp[0] = (dp[0] * 2 + 1) % MOD
            elif nums[i] == 1:
                dp[1] = (dp[0] + dp[1] * 2) % MOD
            else:
                dp[2] = (dp[1] + dp[2] * 2) % MOD
        return dp[2]


if __name__ == '__main__':
    nums = [0, 1, 2, 2]
    nums = [0, 0, 2, 1, 2, 0]
    print(Solution().countSpecialSubsequences(nums))
