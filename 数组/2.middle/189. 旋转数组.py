# -*- coding: utf-8 -*-
# @Time    : 2021/07/27 11:01
# @File    : 189. 旋转数组
from leetcode import *


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
