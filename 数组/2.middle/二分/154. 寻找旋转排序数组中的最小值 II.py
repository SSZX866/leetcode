# -*- coding: utf-8 -*-
# @Time    : 2021/4/9 10:26
# @File    : 154. 寻找旋转排序数组中的最小值 II.py
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        index = len(nums) - 1
        while index != 0 and nums[index] == nums[0]:
            index -= 1
        nums = nums[:index + 1]
        i, j = 0, len(nums)
        while i < j and nums[i] >= nums[0]:
            mid = i + ((j - i) >> 1)
            if nums[mid] >= nums[0]:
                i = mid + 1
            else:
                j = mid
        return nums[i] if i < len(nums) else nums[0]


if __name__ == '__main__':
    nums = [3, 1, 3, 3]
    print(Solution().findMin(nums))
