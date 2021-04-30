# -*- coding: utf-8 -*-
# @Time    : 2021/4/29 20:34
# @File    : 461. 汉明距离.py
from leetcode import *


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        distance = 0
        while xor:
            # mask out the rest bits
            if xor & 1:
                distance += 1
            xor = xor >> 1
        return distance

if __name__ == '__main__':
    x = 1
    y = 4
    print(Solution().hammingDistance(x, y))
