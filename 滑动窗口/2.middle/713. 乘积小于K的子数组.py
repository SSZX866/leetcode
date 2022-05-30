# -*- coding: utf-8 -*-
# @Time    : 2021/8/21 17:13
# @File    : 713. 乘积小于K的子数组.py
from leetcode import *


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0: return k
        ans = 0
        for i in range(len(nums)):
            cur = nums[i]
            if cur >= k: continue
            ans += 1
            for j in range(i + 1, len(nums)):
                cur *= nums[j]
                if cur >= k: break
                ans += 1
        return ans

# 209类似
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 找最小，维护一个小于等于target的窗口，left,right从0开始
        if k <= 1: return 0
        ans = 0
        cur = 1
        left = 0
        for right in range(len(nums)):
            cur *= nums[right]
            while cur >= k:
                cur //= nums[left]
                left += 1
            ans += right - left + 1
        return ans
