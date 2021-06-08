# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 11:07
# @File    : 1049. 最后一块石头的重量 II.py
from leetcode import *


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        print(stones)
        while len(stones) > 1:
            this = stones[0]
            delta = [1000, 0]
            for i in range(1, len(stones)):
                thisDelta = abs(stones[i] - this)
                if thisDelta < delta[0]:
                    delta = [thisDelta, i]
            a = stones.pop(delta[1])
            b = stones.pop(0)
            if a != b:
                stones.append(abs(a - b))
            print(stones, a, b)
        return stones[0]


# 01背包
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        n, m = len(stones), total // 2
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(n):
            for j in range(m + 1):
                if j < stones[i]:
                    dp[i + 1][j] = dp[i][j]
                else:
                    dp[i + 1][j] = dp[i][j] or dp[i][j - stones[i]]

        ans = None
        for j in range(m, -1, -1):
            if dp[n][j]:
                ans = total - 2 * j
                break

        return ans


if __name__ == '__main__':
    stones = [2, 7, 4, 1, 8, 1]
    print(Solution().lastStoneWeightII(stones))
