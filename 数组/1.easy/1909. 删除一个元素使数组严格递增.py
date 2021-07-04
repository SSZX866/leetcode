# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 22:31
# @File    : 5780. 删除一个元素使数组严格递增.py
from leetcode import *


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        i = 1
        flag = False
        N = len(nums)
        while i < N:
            if nums[i] <= nums[i - 1]:
                if flag:
                    return False
                else:
                    N -= 1
                    nums.pop(i)
                    flag = True
                    continue
            i += 1
        return True


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def check(target):
            i = 1
            while i < len(target):
                if target[i] <= target[i - 1]:
                    return False
                i += 1
            return True

        for i in range(len(nums)):
            tmp = nums[:i] + nums[i + 1:]
            if check(tmp): return True
        return False


if __name__ == '__main__':
    nums = [512, 867, 904, 997, 403]
    print(Solution().canBeIncreasing(nums))
