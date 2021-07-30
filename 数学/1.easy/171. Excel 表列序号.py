# -*- coding: utf-8 -*-
# @Time    : 2021/07/30 16:18
# @File    : 171. Excel 表列序号
from leetcode import *


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        table = {chr(each): each - 64 for each in range(65, 91)}
        ans = 0
        for i in range(len(columnTitle)):
            ans += 26 ** i * table[columnTitle[-i - 1]]
        return ans


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for i in range(len(columnTitle)):
            ans += 26 ** i * (ord(columnTitle[-i - 1]) - 64)
        return ans


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # return reduce(lambda x, y: x + y, [26 ** i * (ord(columnTitle[-i - 1]) - 64) for i in range(len(columnTitle))])
        return sum(26 ** i * (ord(columnTitle[-i - 1]) - 64) for i in range(len(columnTitle)))


if __name__ == '__main__':
    columnTitle = "AB"
    columnTitle = "ZY"
    print(Solution().titleToNumber(columnTitle))
