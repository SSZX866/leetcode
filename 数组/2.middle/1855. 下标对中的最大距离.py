# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 15:40
# @File    : 1855. 下标对中的最大距离.py
from leetcode import *


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j, m, n, ans = 0, 0, len(nums1), len(nums2), 0
        for i in range(n):
            while j < m and nums1[j] > nums2[i]:
                j += 1
            if j < m:
                ans = max(i - j, ans)
            else:
                return ans
        return ans


if __name__ == '__main__':
    nums1 = [55, 30, 5, 4, 2]
    nums2 = [100, 20, 10, 10, 5]
    print(Solution().maxDistance(nums1, nums2))
