# -*- coding: utf-8 -*-
# @Time    : 2021/5/29 22:32
# @File    : 5754. 长度为三且各字符不同的子字符串.py
from leetcode import *


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3: return 0
        ans = 0
        for i in range(len(s) - 2):
            a, b, c = ord(s[i]), ord(s[i + 1]), ord(s[i + 2])
            if a != b and b != c and a != c:
                ans += 1
        return ans


if __name__ == '__main__':
    print(Solution().countGoodSubstrings("owuxoelszb"))
