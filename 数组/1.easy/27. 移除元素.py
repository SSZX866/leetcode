# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 10:35
# @File    : 27. 移除元素.py
from leetcode import *

# 对撞指针
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            while i <= j and nums[j] == val:
                j -= 1
            if i > j:
                return i
            if nums[i] == val:
                nums[i] = nums[j]
                nums[j] = val
            i += 1
        return i

# 快慢指针
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = low = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[low] = nums[fast]
                low += 1
            fast += 1
        return low


if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3
    index = Solution().removeElement(nums, val)
    print(nums[:index])
