# -*- coding: utf-8 -*-
# @Time    : 2021/4/5 15:02
# @File    : 1. 采购方案.py
from typing import List


class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0 for _ in nums]
        for i in range(1, len(nums)):
            if nums[i] <= target:
                j = 0
                while j < i:
                    if nums[j] + nums[i] > target:
                        break
                    j += 1
                if j == 1:
                    dp[i] = dp[i - 1] + 1
                elif j == 0:
                    dp[i] = dp[i - 1]
                else:
                    dp[i] = dp[i - 1] + j
            else:
                dp[i] = dp[i - 1]

        return dp[-1] % 1000000007


class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        helps = []
        res = 0
        for num in nums:
            if num < target:
                for help in helps:
                    if num <= help:
                        res += 1
                helps.append(target - num)
        return res % 1000000007


class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        nums.sort()
        i, j, ans = 0, len(nums) - 1, 0
        while i < j:
            while i < j and nums[i] + nums[j] > target:
                j -= 1
            ans += j - i
            i += 1
        return ans%1000000007


if __name__ == '__main__':
    print(Solution().purchasePlans([40330, 31957, 63879, 13204, 47923, 56282, 75126, 3423, 98483], 60482))
