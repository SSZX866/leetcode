# -*- coding: utf-8 -*-
# @Time    : 2021/3/31 18:05
# @File    : 46. 全排列.py
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        def backtrack(path,res,nums):
            if len(nums) == len(path):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtrack(path,res,nums)
                    path.pop()
        path, res = [], []
        backtrack(path,res,nums)
        return res

if __name__ == '__main__':
    print(Solution().permute([1,2,3]))