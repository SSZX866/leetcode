# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 14:18
# @File    : 1389. 按既定顺序创建目标数组.py
from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(index)):
            target.insert(index[i], nums[i])
        return target
