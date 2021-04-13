# -*- coding: utf-8 -*-
# @Time    : 2021/4/5 11:26
# @File    : 88. 合并两个有序数组.py
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = m - 1, n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[i + j + 1] = nums1[i]
                i -= 1
            else:
                nums1[i + j + 1] = nums2[j]
                j -= 1
        while j >= 0:
            nums1[j] = nums2[j]
            j -= 1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 2, 2]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1)
