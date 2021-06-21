# -*- coding: utf-8 -*-
# @Time    : 2021/6/20 10:33
# @File    : 5788. 字符串中的最大奇数.py
from leetcode import *


class Solution:
    def largestOddNumber(self, num: str) -> str:
        tmp = []
        i = 0
        while i < len(num):
            while i < len(num) and int(num[i]) % 2 == 0: i += 1
            this = ''
            j = i
            while j < len(num):
                if int(num[j]) % 2 == 0: break
                this += num[j]
                j += 1
            if this: tmp.append(int(this))
            i = j
        return str(max(tmp)) if tmp else ''


class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = 0
        ans = -1
        while i < len(num):
            if int(num[i]) % 2: ans = i
            i += 1
        return num[:ans + 1]


if __name__ == '__main__':
    "52"
    num = "4206"
    # num = "35427"
    print(Solution().largestOddNumber(num))
