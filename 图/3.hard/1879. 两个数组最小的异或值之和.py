# -*- coding: utf-8 -*-
# @Time    : 2021/5/29 22:52
# @File    : 5756. 两个数组最小的异或值之和.py
from leetcode import *


class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        while i < len(nums1):
            if nums1[i] in nums2:
                nums2.pop(nums2.index(nums1[i]))
                nums1.pop(i)
            else:
                i += 1
        print(nums1, nums2)
        nums = [[]]
        for c in nums2:
            nums = [num[:i] + [c] + num[i:] for num in nums for i in range((num + [c]).index(c) + 1)]
        ans = -1
        for each in nums:
            tmp = 0
            for i in range(len(each)):
                tmp += nums1[i] ^ each[i]
            if ans != -1:
                ans = min(tmp, ans)
            else:
                ans = tmp
        return ans


if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [2, 3]
    # [1,0,3]
    # [5,3,4]
    print(Solution().minimumXORSum(nums1, nums2))
