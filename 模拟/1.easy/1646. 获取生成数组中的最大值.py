# -*- coding: utf-8 -*-
# @Time    : 2021/8/23 13:46
# @File    : 1646. 获取生成数组中的最大值.py
from leetcode import *


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 2: return n
        nums = (n + 1) * [0]
        nums[1] = 1
        for i in range(2, n + 1):
            if i % 2:
                nums[i] = nums[(i - 1) // 2] + nums[((i - 1) // 2) + 1]
            else:
                nums[i] = nums[i // 2]
        return max(nums)
