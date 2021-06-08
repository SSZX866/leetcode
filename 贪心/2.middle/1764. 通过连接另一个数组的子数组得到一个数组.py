# -*- coding: utf-8 -*-
# @Time    : 2021/6/8 15:32
# @File    : 1764. 通过连接另一个数组的子数组得到一个数组.py
from leetcode import *


class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        i, n = 0, len(nums)
        for group in groups:
            groupLength = len(group)
            while i < n - groupLength + 1:
                if nums[i] != group[0] or nums[i:i + groupLength] != group:
                    i += 1
                else:
                    break

            if i >= n - groupLength + 1: return False
            print(nums[i:i + groupLength], i)
            i += groupLength
        return True


if __name__ == '__main__':
    groups = [[1, 2, 3], [3, 4]]
    nums = [7, 7, 1, 2, 3, 4, 7, 7]
    groups = [[1, -1, -1], [3, -2, 0]]
    nums = [1, -1, 0, 1, -1, -1, 3, -2, 0]
    # groups = [[-5, 0]]
    # nums = [2, 0, -2, 5, -1, 2, 4, 3, 4, -5, -5]
    print(Solution().canChoose(groups, nums))
