# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 10:37
# @File    : 377. 组合总和 Ⅳ.py
from leetcode import *


# 回朔 超时
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0

        def backtrace(path):
            nonlocal ans
            if sum(path) == target:
                ans += 1
                return
            elif sum(path) > target:
                return
            for num in nums:
                path.append(num)
                backtrace(path)
                path.pop()

        backtrace([])
        return ans


# 递归 超时
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if target == 0: return 1
        res = 0
        for num in nums:
            if num <= target:
                res += self.combinationSum4(nums, target - num)
        return res


# 记忆化搜索
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [None] * (target + 1)  # 初始化为0会超时，因为有案例中途结果为0，干脆直接初始化为None
        return self.search(nums, target, dp)

    def search(self, nums, target, dp):
        if target == 0:
            dp[0] = 1
        elif dp[target] == None:
            res = 0
            for num in nums:
                if num <= target:
                    res += self.search(nums, target - num, dp)
            dp[target] = res
        return dp[target]


# 根据记忆化搜索 写dp
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(target):
            for num in nums:
                if i + num <= target:
                    dp[i + num] += dp[i]
        return dp[target]


if __name__ == '__main__':
    nums = [1, 2, 3]
    target = 4
    nums = [4, 2, 1]
    target = 32
    nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230,
            240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440,
            450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650,
            660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860,
            870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 111]
    target = 999
    print(Solution().combinationSum4(nums, target))
