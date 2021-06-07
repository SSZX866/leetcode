# -*- coding: utf-8 -*-
# @Time    : 2021/6/6 20:20
# @File    : 1763. 最长的美好子字符串.py
from leetcode import *


class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ''

        def check(target):
            dic = set(target)

            for each in dic:
                thisAci = ord(each)
                if thisAci > 96:  # 小写
                    if chr(thisAci - 32) not in dic:
                        return False
                else:
                    if chr(thisAci + 32) not in dic:
                        return False
            return True

        for i in range(len(s)):
            for j in range(i + 2, len(s) + 1):
                tmpStr = s[i:j]
                if check(tmpStr):
                    ans = tmpStr if len(tmpStr) > len(ans) else ans
        return ans


if __name__ == '__main__':
    s = "YazaAay"
    print(Solution().longestNiceSubstring(s))
