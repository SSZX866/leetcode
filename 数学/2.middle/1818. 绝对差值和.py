# -*- coding: utf-8 -*-
# @Time    : 2021/5/24 11:43
# @File    : 1818. 绝对差值和.py
from leetcode import *


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        delta = [abs(nums1[i] - nums2[i]) for i in range(len(nums1))]
        # delta
        print(delta)


if __name__ == '__main__':
    nums1 = [1, 7, 5, 9]
    nums2 = [2, 3, 5, 13]
    print(Solution().minAbsoluteSumDiff(nums1, nums2))
