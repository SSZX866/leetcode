# -*- coding: utf-8 -*-
# @Time    : 2021/7/9 14:37
# @File    : 面试题 17.10. 主要元素.py
from leetcode import *


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        tmp = max(counter, key=lambda x: counter[x])
        return -1 if counter[tmp] <= len(nums) / 2 else tmp


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur = [nums[0], 1]
        for num in nums[1:]:
            if num == cur[0]:
                cur[1] += 1
            else:
                if not cur[1]:
                    cur = [num, 1]
                else:
                    cur[1] -= 1
        return -1 if nums.count(cur[0]) <= len(nums) / 2 else cur[0]
