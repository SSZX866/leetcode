# -*- coding: utf-8 -*-
# @Time    : 2021/7/11 10:34
# @File    : 5809. 长度为 3 的不同回文子序列.py
from leetcode import *


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        i = 0
        dic = defaultdict(set)
        ans = 0
        while i < n - 1:
            flag = True
            j = n - 1
            while j > i + 1:
                if flag and s[j] != s[i]:
                    j -= 1
                    continue
                flag = False
                if s[j] not in dic[s[i]]:
                    ans += 1
                dic[s[i]].add(s[j])
                j -= 1
            i += 1
        return ans


if __name__ == '__main__':
    s = "aaa"
    s = "bbcbaba"
    print(Solution().countPalindromicSubsequence(s))
