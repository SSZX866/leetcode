# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 21:16
# @File    : 面试题 08.04. 幂集.py
from leetcode import *


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrace(path, res, nums, i):
            print(path,nums)
            res.append(path[:])
            for i in range(i,len(nums)):
                path.append(nums[i])
                backtrace(path, res, nums, i + 1)
                path.pop()

        res = []
        backtrace([], res, nums, 0)
        return res
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res, path = [], []
#
#         def backtrack(index, nums, res, path):
#             res.append(path[:])
#             for i in range(index, len(nums)):
#                 path.append(nums[i])
#                 backtrack(i + 1, nums, res, path)
#                 path.pop()
#
#         backtrack(0, nums, res, path)
#         return res

if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().subsets(nums))
