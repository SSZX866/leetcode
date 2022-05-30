# -*- coding: utf-8 -*-
# @Time    : 2021/6/12 22:37
# @File    : 5768. 找到需要补充粉笔的学生编号.py
from leetcode import *


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        Sum = sum(chalk)
        k %= Sum

        for i in range(len(chalk)):
            if k == 0: return i
            k -= chalk[i]
            if k < 0: return i
        return 0


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k %= sum(chalk)
        for i in range(len(chalk)):
            k -= chalk[i]
            if k >= 0: continue
            return i
        return 0


if __name__ == '__main__':
    chalk = [3, 4, 1, 2]
    k = 25
    print(Solution().chalkReplacer(chalk, k))
