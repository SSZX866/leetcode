# -*- coding: utf-8 -*-
# @Time    : 2021/4/9 22:33
# @File    : 34. 在排序数组中查找元素的第一个和最后一个位置.py
# ——————————————————————————————
#            8  8
# nums[mid]<=target 区间取的左半部分，所以i为最后出现的<=target的下标，及最后一次出现8的位置
# ---------------
# ——————————————————————————————
#            8  8
# nums[mid]>=target 区间取的右半部分，所以i为最后出现的>=target的下标，及第一次出现8的位置
#            ---------------—---
# ——————————————————————————————
#            8  8
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        i, j = 0, len(nums)
        while i < j:
            mid = i + ((j - i) >> 1)
            if nums[mid] >= target:
                j = mid
            else:
                i = mid + 1
        ans = [i, 0]
        j = len(nums)
        while i < j:
            mid = i + ((j - i) >> 1)
            if nums[mid] > target:
                j = mid
            else:
                i = mid + 1
        ans[1] = j - 1
        return ans if nums[j - 1] == target else [-1, -1]


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 3, 4, 5]
    target = 2
    print(Solution().searchRange(nums, target))
