# -*- coding: utf-8 -*-
# @Time    : 2021/4/21 23:09
# @File    : 1689. 十-二进制数的最少数目.py
from leetcode import *
class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))

if __name__ == '__main__':
    n = "32"
    print(Solution().minPartitions(n))