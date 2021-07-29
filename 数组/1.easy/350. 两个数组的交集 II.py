# -*- coding: utf-8 -*-
# @Time    : 2021/07/28 13:07
# @File    : 350. 两个数组的交集 II
from leetcode import *


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = Counter(nums1) & Counter(nums2)
        ans = []
        for key in counter.keys():
            ans.extend([key] * counter[key])
        return ans
