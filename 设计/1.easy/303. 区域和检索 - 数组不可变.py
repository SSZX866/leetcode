# -*- coding: utf-8 -*-
# @Time    : 2021/3/19 10:08
# @File    : 303. 区域和检索 - 数组不可变.py
from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])