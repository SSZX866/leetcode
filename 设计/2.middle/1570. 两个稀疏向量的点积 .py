# -*- coding: utf-8 -*-
# @Time    : 2021/7/8 21:16
# @File    : 1570. 两个稀疏向量的点积.py
from leetcode import *


class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for i in range(len(self.nums)):
            ans += self.nums[i] * vec.nums[i]
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
