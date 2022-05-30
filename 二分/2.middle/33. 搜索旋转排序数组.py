# -*- coding: utf-8 -*-
# @Time    : 2021/4/8 11:20
# @File    : 33. 搜索旋转排序数组.py
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j, mid = 0, len(nums), -1
        while i < j and nums[i] >= nums[0]:
            mid = i + ((j - i) >> 1)
            if nums[mid] >= nums[0]:
                i = mid + 1
            else:
                j = mid
        ans = self.binSearch(nums[:i], target), self.binSearch(nums[i:], target)
        return ans[1] + i if ans[1] != -1 else ans[0]

    def binSearch(self, nums, target):
        if not nums: return -1
        i, j = 0, len(nums)
        while i < j:
            mid = i + ((j - i) >> 1)
            if target > nums[mid]:
                i = mid + 1
            else:
                j = mid
        return i if i < len(nums) and nums[i] == target else -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target: return mid
            #  前半部分有序
            if nums[0] < nums[mid]:
                if nums[0] <= target < nums[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            #  后半部分有序
            else:
                if nums[mid] < target <= nums[-1]:
                    lo = mid + 1
                else:
                    hi = mid
        return lo if lo != len(nums) and nums[lo] == target else -1


if __name__ == '__main__':
    nums = [2, 1]
    target = 1
    print(Solution().search(nums, target))
