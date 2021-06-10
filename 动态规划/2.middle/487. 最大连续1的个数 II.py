# -*- coding: utf-8 -*-
# @Time    : 2021/6/10 11:31
# @File    : 487. 最大连续1的个数 II.py
from leetcode import *


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        dp = [[0] * 2 for _ in nums]
        # dp[i][0] 以当前结尾没有使用过权利的最大1的个数
        # dp[i][1] 以当前结尾使用过权利的最大1的个数
        dp[0][0] = nums[0]
        # dp[0][1] = 1
        dp[0][1] = -9999999 if nums[0] else 1
        for i in range(1, len(nums)):
            if nums[i] == 0:
                dp[i][0] = 0
                dp[i][1] = dp[i - 1][0] + 1
            else:
                dp[i][0] = dp[i - 1][0] + 1
                dp[i][1] = dp[i - 1][1] + 1
        # return max(list(zip(*dp))[1])
        return max(max(list(zip(*dp))[1]), max(list(zip(*dp))[0]))


if __name__ == '__main__':
    nums = [1, 0, 1, 1, 0]
    nums = [0]
    print(Solution().findMaxConsecutiveOnes(nums))
