# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 21:11
# @File    : 面试题 16.01. 交换数字.py
from leetcode import *


# a = b - a
# b = b - a --->原先的a
# a = a + b
class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        numbers[0] = numbers[1] - numbers[0]
        numbers[1] = numbers[1] - numbers[0]
        numbers[0] = numbers[1] + numbers[0]
        return numbers
