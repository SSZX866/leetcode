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


class Solution(object):
    def subsetsWithDup(self, nums):
        res, path = [], []
        nums.sort()
        self.dfs(nums, 0, res, path)
        return res

    def dfs(self, nums, index, res, path):
        res.append(copy.deepcopy(path))
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.dfs(nums, i + 1, res, path)
            path.pop()


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n, ans = len(nums), []

        def backtrack(path, index, dic, cur):
            ans.append(path[:])
            for i in range(index, n):
                new = cur + str(nums[i])
                if new in dic:
                    continue
                dic.add(new)
                path.append(nums[i])
                backtrack(path, i + 1, dic, new)
                path.pop()

        nums.sort()
        backtrack([], 0, set(), '1' + '0' * 30)
        return ans


if __name__ == '__main__':
    nums = [4, 4, 4, 1, 4]
    print(Solution().subsetsWithDup(nums))
