# -*- coding: utf-8 -*-
# @Time    : 2021/5/16 10:39
# @File    : 5760. 构成交替字符串需要的最小交换次数.py
from leetcode import *


class Solution:
    def minSwaps(self, s: str) -> int:
        s, ans = [x for x in s], -1
        s = [s[0]] + s + [s[len(s) - 1]]
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                tmp = ans
                for j in range(i, len(s)):
                    if s[j] == s[j - 1] and s[j] != s[i]:
                        s[i], s[j] = s[j], s[i]
                        ans += 1
                if ans == tmp:
                    return -1
        return ans


class Solution:
    def minSwaps(self, s: str) -> int:
        one, zero, n, cnt = s.count('1'), s.count('0'), len(s), 0
        if abs(one - zero) > 1: return -1
        target = ''.join(['1' if i % 2 else '0' for i in range(n)]) if one <= zero else ''.join(
            ['0' if i % 2 else '1' for i in range(n)])
        for i in range(n):
            if s[i] != target[i]: cnt += 1
        cnt, ans = 0, cnt
        if one == zero:
            target = ''.join(['0' if i % 2 else '1' for i in range(n)])
            for i in range(n):
                if s[i] != target[i]: cnt += 1
            ans = min(cnt, ans)
        return ans//2


if __name__ == '__main__':
    print(Solution().minSwaps('100'))
    print(Solution().minSwaps("111000"))
