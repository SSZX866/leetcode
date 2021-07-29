# -*- coding: utf-8 -*-
# @Time    : 2021/07/28 12:14
# @File    : 167. 两数之和 II - 输入有序数组
from leetcode import *


# 对撞指针
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right += 1
