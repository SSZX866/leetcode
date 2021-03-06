# -*- coding: utf-8 -*-
# @Time    : 2021/3/31 20:52
# @File    : 77. 组合.py
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(res, path, left, right, k):
            if len(path) == k:
                res.append(path[:])
                return
            # for i in range(left, right): 剪枝
            for i in range(left, right - (k - len(path)) + 1):
                path.append(i)
                backtrack(res, path, i + 1, right, k)
                path.pop()

        res, path = [], []
        backtrack(res, path, 1, n + 1, k)
        return res


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        nums = [i + 1 for i in range(n)]

        def backtrack(path, i):
            if len(path) == k:
                ans.append(path[:])
                return
            for i in range(i, len(nums)):
                path.append(nums[i])
                backtrack(path, i + 1)
                path.pop()

        backtrack([], 0)
        return ans


if __name__ == '__main__':
    print(Solution().combine(4, 2))
