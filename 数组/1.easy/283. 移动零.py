# -*- coding: utf-8 -*-
# @Time    : 2021/07/28 11:23
# @File    : 283. 移动零
from leetcode import *


#  快慢指针
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[n] = nums[i]
                n = n + 1
        for i in range(n, len(nums)):
            nums[i] = 0


#  双指针
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, i = 0, 0
        n = len(nums)

        def findZero(zero):
            while zero < n:
                if not nums[zero]:
                    break
                zero += 1
            return zero if zero < n else -1

        def findNotZero(i):
            while i < n:
                if nums[i]:
                    break
                i += 1
            return i if i < n else -1

        zero = findZero(zero)
        if zero == -1: return
        i = findNotZero(i)
        if i == -1: return
        while i != -1 and zero != -1:
            while i != -1 and not nums[i]:
                i = findNotZero(i + 1)
            if i == -1: return
            if i < zero:
                i += 1
                continue
            nums[i], nums[zero] = nums[zero], nums[i]
            zero = min(i, findZero(zero + 1))


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    nums = [1, 0]
    Solution().moveZeroes(nums)
    print(nums)
