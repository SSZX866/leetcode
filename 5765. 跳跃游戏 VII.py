# -*- coding: utf-8 -*-
# @Time    : 2021/5/23 10:42
# @File    : 5765. 跳跃游戏 VII.py
from leetcode import *


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [False] * len(s)
        dp[0] = True
        for i in range(1, len(s)):
            if i < maxJump and s[i] == '0':
                if i >= minJump:
                    dp[i] = functools.reduce(lambda x, y: x or y, dp[0:i - minJump + 1])
            elif s[i] == '0':
                dp[i] = functools.reduce(lambda x, y: x or y, dp[i - maxJump:i - minJump + 1])
        return dp[-1]


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [False] * len(s)
        pre = [0] * (len(s)+1)
        dp[0] = True
        pre[1] = 1
        for i in range(1, len(s)):
            if i <= maxJump and s[i] == '0':
                if i >= minJump:
                    # dp[i] = functools.reduce(lambda x, y: x or y, dp[0:i - minJump + 1])
                    dp[i] = (pre[i - minJump+1]) > 0
            elif s[i] == '0':
                # dp[i] = functools.reduce(lambda x, y: x or y, dp[i - maxJump:i - minJump + 1])
                dp[i] = (pre[i - minJump+1] - pre[i - maxJump]) > 0
            pre[i+1] = pre[i] + bool(dp[i])
        print(pre,dp)
        return dp[-1]


if __name__ == '__main__':
    s = "011010"
    minJump = 2
    maxJump = 3
    s = "00"
    minJump = 1
    maxJump = 1
    print(Solution().canReach(s, minJump, maxJump))
