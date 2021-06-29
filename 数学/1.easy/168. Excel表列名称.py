# -*- coding: utf-8 -*-
# @Time    : 2021/6/29 17:14
# @File    : 168. Excel表列名称.py
from leetcode import *


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        dic = {i + 1: chr(65 + i) for i in range(26)}
        ans = ''
        while columnNumber:
            columnNumber -= 1
            ans += dic[(columnNumber % 26) + 1]
            columnNumber //= 26
        return ans[::-1]


if __name__ == '__main__':
    print(Solution().convertToTitle(columnNumber=28))
