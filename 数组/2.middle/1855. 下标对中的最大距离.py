# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 15:40
# @File    : 1855. 下标对中的最大距离.py
from leetcode import *


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j, m, n, ans = 0, 0, len(nums1), len(nums2), 0
        while i < m:
            j = i
            # while j < n:
            #     if nums2[j] >= nums1[i]:
            #         ans = max(j - i, ans)
            #     j += 1
            lo, hi = j, n
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if nums2[mid] < nums1[i]:
                    lo = mid + 1
                else:
                    hi = mid
                print(lo)
                ans = max(j - i, ans)
            i += 1
        return ans
if __name__ == '__main__':
    nums1 = [55, 30, 5, 4, 2]
    nums2 = [100, 20, 10, 10, 5]
    print(Solution().maxDistance(nums1,nums2))