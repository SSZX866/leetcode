# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 14:32
# @File    : 1780. 判断一个数字是否可以表示成三的幂的和.py
from leetcode import *


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n < 1: return False
        tmp = 1
        while tmp < n:
            tmp *= 3
        if tmp == n:
            return True
        return n - tmp // 3 < tmp // 3 and self.checkPowersOfThree(n - tmp // 3)


class Solution:
    def __init__(self):
        self.help = [1]
        for i in range(15):
            self.help.append(self.help[-1] * 3)

    def checkPowersOfThree(self, n: int) -> bool:
        if n < 1: return False
        tmp = self.help[bisect.bisect(self.help, n)]
        if tmp // 3 == n:
            return True
        return n - tmp // 3 < tmp // 3 and self.checkPowersOfThree(n - tmp // 3)


if __name__ == '__main__':
    print(Solution().checkPowersOfThree(91))
