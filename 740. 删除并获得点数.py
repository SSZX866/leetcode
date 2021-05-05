# -*- coding: utf-8 -*-
# @Time    : 2021/05/05 12:56
# @File    : 740. 删除并获得点数.py
from collections import Counter

from leetcode import *


# 递归
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        return self.call(nums)

    def process(self, nums, i):
        tmp = []
        for num in nums[:i] + nums[i + 1:]:
            if num != nums[i] - 1 and num != nums[i] + 1:
                tmp.append(num)
        return tmp

    def call(self, nums):
        if len(nums) == 1: return nums[0]
        ans = 0
        for i, num in enumerate(nums):
            ans = max(self.deleteAndEarn(self.process(nums, i)) + num, ans)
        return ans


# dp
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp, tmp, counter = [0] * (max(nums) + 1), [0] * (max(nums) + 1), Counter(nums)
        for key in counter:
            tmp[key] = counter[key]
        # for num in nums:
        #     tmp[num] += 1
        dp[1] = tmp[1]
        for i in range(2, max(nums) + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + i * tmp[i])
        return dp[-1]


if __name__ == '__main__':
    nums = [3, 4, 2]
    nums = [2, 2, 3, 3, 3, 4]
    print(Solution().deleteAndEarn(nums))
