# -*- coding: utf-8 -*-
# @Time    : 2021/6/6 10:58
# @File    : 5778. 使二进制字符串字符交替的最少反转次数.py
from leetcode import *


# 101
# 010
class Solution:
    def minFlips(self, s: str) -> int:
        if len(s) == 1: return 0
        ans = 0
        i = 1
        n = len(s)
        while i < n:
            cnt, tmp = 1, s[:i]
            while i < n and s[i] == s[i - 1]:
                tmp += str(int(tmp[-1]) ^ 1)
                cnt += 1
                i += 1
            if i < n:
                tmp += s[i:]
                if s[i]!=tmp[i-1]:i += 1
                s = tmp
            ans += cnt//2
        return ans


if __name__ == '__main__':
    s = "10010011010"

    print(Solution().minFlips(s))
