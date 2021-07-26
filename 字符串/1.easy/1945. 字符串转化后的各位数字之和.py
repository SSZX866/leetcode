# -*- coding: utf-8 -*-
# @Time    : 2021/07/26 11:07
# @File    : 1945. 字符串转化后的各位数字之和
from leetcode import *


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        tmp = ''.join([str(ord(each) - 97) for each in s])
        while k or len(s) != 1:
            tmp = str(sum(map(int, tmp)))
            k -= 1
        return int(tmp)
