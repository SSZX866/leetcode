# -*- coding: utf-8 -*-
# @Time    : 2021/7/8 20:56
# @File    : 152. 乘积最大子数组.py
from leetcode import *


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        reverse_nums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            reverse_nums[i] *= reverse_nums[i - 1] or 1
        return max(nums + reverse_nums)


if __name__ == '__main__':
    nums = [2, 3, -2, 4]
    nums = [-2,0,-1]
    print(Solution().maxProduct(nums))
