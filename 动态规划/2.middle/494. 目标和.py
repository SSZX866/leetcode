# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 08:52
# @File    : 494. 目标和.py
import copy

from leetcode import *


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans = 0
        tmp = [[]]
        pre = 0
        for num in nums:
            n = len(tmp)
            for i in range(pre, n):
                tmp.append(tmp[i] + [+num])
                tmp.append(tmp[i] + [-num])
            # print(tmp)
            pre = n
        for each in tmp[n:]:
            if sum(each) == target:
                ans += 1
                # print(each)
        return ans


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans = 0
        tmp = [[]]
        for num in nums:
            n = len(tmp)
            tmp = copy.deepcopy(tmp) + copy.deepcopy(tmp)
            for i in range(n):
                tmp[i].append(+num)
            for i in range(n, 2 * n):
                tmp[i].append(-num)
        for each in tmp:
            if sum(each) == target:
                ans += 1
        return ans


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans = 0
        tmp = [0]
        pre = 0
        for num in nums:
            n = len(tmp)
            for i in range(pre, n):
                tmp.append(tmp[i] + +num)
                tmp.append(tmp[i] + -num)
            # print(tmp)
            pre = n
        for each in tmp[n:]:
            if each == target:
                ans += 1
                # print(each)
        return ans


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans = 0
        tmp = [0]
        for num in nums:
            n = len(tmp)
            tmp = tmp + tmp
            for i in range(n):
                tmp[i] += (+num)
            for i in range(n, 2 * n):
                tmp[i] += (-num)
            # print(tmp)
        for each in tmp:
            if each == target:
                ans += 1
        return ans


# 集合运算           sum(P) - sum(N) = target
# sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)
#                        2 * sum(P) = target + sum(nums)
# 01背包
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 正数和为x，负数和绝对值为y   x + y = sum(nums)  x - y = target   x = (sum+target)/2
        tot_sum = sum(nums)
        if tot_sum < target:
            return 0
        positive_sum = (tot_sum + target) // 2
        if (tot_sum + target) % 2 == 1:
            return 0

        dp = [0 for _ in range(positive_sum + 1)]
        dp[0] = 1
        for num in nums:
            for x in range(positive_sum, num - 1, -1):
                dp[x] += dp[x - num]
        return dp[positive_sum]


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(index, cur):
            if index == n:
                return int(cur == target)
            return dfs(index + 1, cur + nums[index]) + dfs(index + 1, cur - nums[index])

        return dfs(0, 0)


# 01背包
# dp[i][s] 在前i个元素子集中添加符号，所得值恰好为s时有多少种不同的方法
# s可能是负数，而s作为数组的index不能为负。解决方法就是给s加上一个SUM的偏移，将[-SUM,SUM]的区间平移至[0,SUM*2]作为DP数组的第二个维度的index
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        dp = [[0] * (total * 2 + 1) for _ in range(len(nums))]
        if abs(target) > total: return 0
        dp[0][nums[0] + total] = dp[0][-nums[0] + total] = 1
        for i in range(1, len(nums)):
            for s in range(-total, total + 1):
                index = s + total
                s1 = s - nums[i]
                if abs(s1) <= total: dp[i][index] += dp[i - 1][s1 + total]
                s2 = s + nums[i]
                if abs(s2) <= total: dp[i][index] += dp[i - 1][s2 + total]

        return dp[-1][target + total]


# 增加偏移
class Solution:
    def findTargetSumWays(self, nums, target):
        total = sum(nums)
        if abs(target) > total: return 0

        N = len(nums)
        dp = [[0 for _ in range(2 * total + 1)] for _ in range(N)]
        dp[0][nums[0] + total] += 1
        dp[0][-nums[0] + total] += 1

        for i in range(1, N):
            for s in range(-total, total + 1):
                s1 = s + nums[i]
                s2 = s - nums[i]

                if (abs(s1) <= total): dp[i][s + total] += dp[i - 1][s1 + total]
                if (abs(s2) <= total): dp[i][s + total] += dp[i - 1][s2 + total]

        return dp[N - 1][target + total]


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    target = 3
    nums = [29, 6, 7, 36, 30, 28, 35, 48, 20, 44, 40, 2, 31, 25, 6, 41, 33, 4, 35, 38]
    target = 35
    nums = [7, 7, 17, 1, 46, 38, 8, 32, 35, 18, 43, 48, 9, 17, 6, 6, 42, 10, 2, 32]
    target = 38
    print(Solution().findTargetSumWays(nums, target))
