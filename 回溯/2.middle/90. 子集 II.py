# -*- coding: utf-8 -*-
# @Time    : 2021/3/31 15:28
# @File    : 90. 子集 II.py
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []

        def backtrack(index, path, nums, result):
            if path not in result:
                result.append(path[:])
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path, nums, result)
                path.pop()
        path, result = [], []
        nums.sort()
        backtrack(0, path, nums, result)
        return result


if __name__ == '__main__':
    nums = [4,4,4,1,4]
    print(Solution().subsetsWithDup(nums))
