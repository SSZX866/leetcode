# -*- coding: utf-8 -*-
# @Time    : 2021/4/28 16:40
# @File    : 1342. 将数字变成 0 的操作次数.py
from leetcode import *


class Solution:
    def numberOfSteps(self, num: int) -> int:
        if not num: return num
        ans = 0
        while num:
            ans += 1 + num % 2
            num >>= 1

        return ans - 1


if __name__ == '__main__':
    num = 1
    print(Solution().numberOfSteps(num))
