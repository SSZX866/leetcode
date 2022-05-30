# -*- coding: utf-8 -*-
# @Time    : 2021/9/27 11:47
# @File    : 639. 解码方法 II.py
from leetcode import *


class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def helper(targetS):
            stack = [targetS]
            tmp = []
            while stack:
                tmpS = stack.pop()
                if '*' not in tmpS:
                    tmp.append(tmpS)
                    continue
                index = tmpS.index('*')
                for i in range(1, 10):
                    newS = tmpS[:index] + str(i) + tmpS[index + 1:]
                    stack.append(newS)

            total = 0
            for target in tmp:
                n = len(target)
                dp = [0] * n
                dp[0] = 0 if s[0] == '0' else 1
                if n == 1:
                    total += dp[-1]
                    continue
                if '0' < target[0] < '2' or (target[0] == '2' and '0' <= target[1] <= '6'):
                    dp[1] = 2 if target[1] != '0' else 1
                elif target[0] == '0':
                    return 0
                else:
                    dp[1] = 1 if target[1] != '0' else 0
                for i in range(2, n):
                    # 单独成码
                    if target[i - 1] == '0':
                        if target[i] == '0': break
                        dp[i] = dp[i - 1]
                    elif target[i - 1] < '2' or (target[i - 1] == '2' and '0' <= target[i] <= '6'):
                        if target[i - 1] == '2' and target[i] == '0':
                            dp[i] = dp[i - 2]
                        else:
                            if target[i] != '0':
                                dp[i] = dp[i - 1] + dp[i - 2]
                            else:
                                dp[i] = dp[i - 2]
                    else:
                        if target[i] != '0': dp[i] = dp[i - 1]
                total += dp[-1]
            return total

        # if len(s) < 3: return helper(s)
        # pre, cur = helper(s[:1]), helper(s[:2])
        # MOD = 1000000007
        # for i in range(2, len(s)):
        #     pre, cur = cur % MOD, (pre * helper(s[i - 2:i]) + cur * helper(s[i])) % MOD
        return helper(s) % 1000000007


ONE = {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, '9': 1, '*': 9}
TWO = {'10': 1, '11': 1, '12': 1, '13': 1, '14': 1, '15': 1, '16': 1, '17': 1, '18': 1, '19': 1, '20': 1,
       '21': 1, '22': 1, '23': 1, '24': 1, '25': 1, '26': 1, '*0': 2, '*1': 2, '*2': 2, '*3': 2, '*4': 2,
       '*5': 2, '*6': 2, '*7': 1, '*8': 1, '*9': 1, '1*': 9, '2*': 6, '**': 15}


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = 1, ONE.get(s[:1], 0)
        for i in range(1, len(s)):
            dp = dp[1], (ONE.get(s[i], 0) * dp[1] + TWO.get(s[i - 1: i + 1], 0) * dp[0]) % 1000000007
        return dp[-1]
