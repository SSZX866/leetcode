# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 11:08
# @File    : 1954. 收集足够苹果的最小花园周长.py
from leetcode import *


class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        n = 1
        while 2 * n * (n + 1) * (2 * n + 1) < neededApples:
            n += 1
        return n * 8



if __name__ == '__main__':
    print(Solution().minimumPerimeter(neededApples=1000000000))
    print(Solution().minimumPerimeter(neededApples=13))
