# -*- coding: utf-8 -*-
# @Time    : 2021/5/16 10:30
# @File    : 5759. 找出所有子集的异或总和再求和.py
from leetcode import *


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res, path = [], []

        def backtrack(index, nums, res, path):
            res.append(path[:])
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, nums, res, path)
                path.pop()

        backtrack(0, nums, res, path)
        ans = 0
        for num in res:
            tmp = 0
            for each in num:
                tmp ^= each
            ans += tmp
        return ans


if __name__ == '__main__':
    nums = [1, 3]
    nums = [1, 1, 1]
    print(Solution().subsetXORSum(nums))
