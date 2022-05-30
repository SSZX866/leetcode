# -*- coding: utf-8 -*-
# @Time    : 2021/11/15 09:04
# @File    : 319. 灯泡开关.py
from leetcode import *


class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n == 0 or n == 1: return n
        tmp = int(math.sqrt(n))
        return self.bulbSwitch(n - 1) + 1 if tmp ** 2 == n else self.bulbSwitch(n - 1)


class Solution:
    def bulbSwitch(self, n: int) -> int:
        res = 0
        for i in range(n):
            tmp = int(math.sqrt(i))
            if tmp ** 2 == i: res += 1
        return res

# 1. 每次某个灯被开关，是当前遍历的i为它的因子
# 2. 某个灯被开关奇数次最后会亮着，偶数次最后会熄灭
# 3. 某个数的因子个数为奇数个，它的所有质因子都出现了偶数次（完全平方数）
# 小于等于n的完全平方数个数为，1^2 .. 2^2 .. ... sqrt(n) ^ 2,  即sqrt(n)

class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))


if __name__ == '__main__':
    print(Solution().bulbSwitch(999999))
