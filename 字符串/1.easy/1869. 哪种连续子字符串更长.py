# -*- coding: utf-8 -*-
# @Time    : 2021/5/23 10:33
# @File    : 5763. 哪种连续子字符串更长.py
from leetcode import *
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        print(s.split('1'),max(s.split('1'),key=len))
        print(s.split('0'),max(s.split('0'),key=len))
        return len(max(s.split('1'),key=len))<len(max(s.split('0'),key=len))
if __name__ == '__main__':
    s="1101"
    "111000"
    "110100010"
    print(Solution().checkZeroOnes(s))