# -*- coding: utf-8 -*-
# @Time    : 2021/7/14 12:57
# @File    : 1818. 绝对差值和.py
from leetcode import *


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        tmp_nums = sorted(nums1)
        max_delta = [0, 0]
        ans = 0

        # 找到nums1中和nums2[i]最近的差值
        def findNearNum(target):
            lo, hi = 0, len(tmp_nums)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if tmp_nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            if lo == 0: return abs(tmp_nums[lo] - target)
            if lo == len(tmp_nums): return abs(tmp_nums[lo - 1] - target)
            return min(abs(tmp_nums[lo] - target), abs(tmp_nums[lo - 1] - target))

        for i in range(len(nums2)):
            delta = abs(nums2[i] - nums1[i])
            ans += delta
            tmp = findNearNum(nums2[i])
            if tmp < delta:
                max_delta = max(max_delta, [tmp, delta - tmp], key=lambda x: x[1])
        return int((ans - max_delta[1]) % (1e9 + 7))


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        tmp_nums = sorted(nums1)
        max_delta = 0  # 记录最大的差值
        ans = 0

        # 找到nums1中和nums2[i]最近的差值
        def findNearNum(target):
            lo, hi = 0, len(tmp_nums)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if tmp_nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            if lo == 0: return abs(tmp_nums[lo] - target)
            if lo == len(tmp_nums): return abs(tmp_nums[lo - 1] - target)
            return min(abs(tmp_nums[lo] - target), abs(tmp_nums[lo - 1] - target))

        for i in range(len(nums2)):
            delta = abs(nums2[i] - nums1[i])
            ans += delta
            tmp = findNearNum(nums2[i])
            if tmp < delta:
                max_delta = max(max_delta, delta - tmp)
        return int((ans - max_delta) % (1e9 + 7))


if __name__ == '__main__':
    nums1 = [1, 7, 5]
    nums2 = [2, 3, 5]
    nums1 = [1, 10, 4, 4, 2, 7]
    nums2 = [9, 3, 5, 1, 7, 4]
    print(Solution().minAbsoluteSumDiff(nums1, nums2))
