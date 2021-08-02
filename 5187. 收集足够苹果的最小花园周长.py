# -*- coding: utf-8 -*-
# @Time    : 2021/8/1 11:08
# @File    : 5187. 收集足够苹果的最小花园周长.py
from leetcode import *


class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        tmp = 12
        x = 2
        while tmp < neededApples:
            tmp = 2 * tmp + (x+1) * 4 + (x + 2) * 4 + x*8
            x += 2
            print(x,tmp)
        return x * 4


if __name__ == '__main__':
    print(Solution().minimumPerimeter(neededApples=1000000000))
    print(Solution().minimumPerimeter(neededApples=13))
