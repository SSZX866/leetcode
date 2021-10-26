# -*- coding: utf-8 -*-
# @Time    : 2021/10/26 11:50
# @File    : 496. 下一个更大元素 I.py
from leetcode import *


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        dic = {nums2[i]: i for i in range(n)}
        ans = []
        for num in nums1:
            i = dic[num]
            while i < n and nums2[i] <= num: i += 1
            if i == n:
                ans.append(-1)
            else:
                ans.append(nums2[i])

        return ans


# 单调栈
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        window, d = [], dict()
        for num in nums2:
            while window and window[-1] < num:
                small = window.pop()
                d[small] = num
            window.append(num)
        return [d[num] if num in d else -1 for num in nums1]
