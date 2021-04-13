# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 11:22
# @File    : 4. 寻找两个正序数组的中位数.py
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if not nums1: return float(nums2[n // 2]) if n % 2 == 1 else (nums2[n // 2] + nums2[n // 2 - 1]) / 2
        if not nums2: return float(nums1[m // 2]) if m % 2 == 1 else (nums1[m // 2] + nums1[m // 2 - 1]) / 2
        i, j, nums = 0, 0, []
        while i < m and j < n:
            while i < m and j < n and nums2[j] > nums1[i]:
                nums.append(nums1[i])
                i += 1
            while j < n and i < m and nums2[j] <= nums1[i]:
                nums.append(nums2[j])
                j += 1
        if j < n:
            nums += nums2[j:]
        if i < m:
            nums += nums1[i:]
        n = len(nums)
        return float(nums[n // 2]) if n % 2 == 1 else (nums[n // 2] + nums[n // 2 - 1]) / 2


if __name__ == '__main__':
    nums1 = [4, 5, 6, 8, 9]
    nums2 = []
    print(Solution().findMedianSortedArrays(nums1, nums2))
