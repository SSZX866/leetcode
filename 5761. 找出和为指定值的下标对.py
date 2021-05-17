# -*- coding: utf-8 -*-
# @Time    : 2021/5/16 10:41
# @File    : 5761. 找出和为指定值的下标对.py
from leetcode import *


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        tmp1, tmp2 = [[nums1[i], i] for i in range(len(nums1))], [[nums2[i], i] for i in range(len(nums2))]
        self.nums1 = sorted(tmp1, key=lambda x: x[0])
        self.nums2 = sorted(tmp2, key=lambda x: x[0])

    def add(self, index: int, val: int) -> None:
        for i in range(len(self.nums2)):
            if self.nums2[i][1] == index:
                tmp = self.nums2.pop(i)
                tmp[0] += val
                lo, hi = 0, len(self.nums2)
                while lo < hi:
                    mid = lo + (hi - lo) // 2
                    if self.nums2[mid][0] < tmp[0]:
                        lo = mid + 1
                    else:
                        hi = mid
                self.nums2 = self.nums2[:hi] + tmp + self.nums2[hi:]
            break

    def count(self, tot: int) -> int:
        ans, lo, hi = 0, 0, len(self.nums2) - 1
        while lo < len(self.nums1) and hi >= 0:
            if self.nums1[lo][0] + self.nums2[hi][0] == tot:
                a = b = 1
                while lo + 1 < len(self.nums1) and self.nums1[lo + 1][0] == self.nums1[lo][0]:
                    lo += 1
                    a += 1
                while hi - 1 >= 0 and self.nums2[hi - 1][0] == self.nums2[hi][0]:
                    hi -= 1
                    b += 1
                ans += a * b
            elif self.nums1[lo][0] + self.nums2[hi][0] < tot:
                if lo + 1 < len(self.nums1) and hi - 1 >= 0 and self.nums1[lo + 1][0] - self.nums1[lo][0] > \
                        self.nums2[hi][0] - self.nums2[hi - 1][0]:
                    hi -= 1
                elif lo + 1 < len(self.nums1) and hi - 1 >= 0 and self.nums1[lo + 1][0] - self.nums1[lo][0] <= \
                        self.nums2[hi][0] - self.nums2[hi - 1][0]:
                    lo += 1
                elif lo + 1 >= len(self.nums1):
                    hi -= 1
                elif hi - 1 <= 0:
                    lo += 1
                else:
                    break
            elif self.nums1[lo][0] + self.nums2[hi][0] > tot:
                hi -= 1
        return ans
