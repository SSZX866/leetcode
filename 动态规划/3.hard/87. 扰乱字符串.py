# -*- coding: utf-8 -*-
# @Time    : 2021/4/16 09:49
# @File    : 87. 扰乱字符串.py
# dp[i][j][length] 从i开始长度为length的字符串和从j开始长度为length是否为扰乱字符串
import functools


class Solution:
    @functools.lru_cache(None)
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False

        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or \
                    (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])):
                return True
        return False


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2): return False
        n = len(s1)
        dp = [[[False] * (n + 1) for _ in range(n)] for __ in range(n)]
        for i in range(n):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[i][j][1] = True
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                for j in range(n - length + 1):
                    for k in range(1, length):
                        if dp[i][j][k] and dp[i + k][j + k][length - k]:
                            dp[i][j][length] = True
                            break
                        if dp[i][j + length - k][k] and dp[i + k][j][length - k]:
                            dp[i][j][length] = True
                            break
        # print(dp)
        return dp[0][0][n]


if __name__ == '__main__':
    s1 = "great"
    s2 = "rgeat"
    print(Solution().isScramble(s1, s2))
