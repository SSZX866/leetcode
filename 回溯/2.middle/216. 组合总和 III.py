# -*- coding: utf-8 -*-
# @Time    : 2021/4/1 10:19
# @File    : 216. 组合总和 III.py
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(res, path, startIndex, k, n):
            if len(path) == k:
                if sum(path) == n:
                    res.append(path[:])
                return
            if sum(path) >= n:
                return
            for i in range(startIndex, n):
                if i > 9:
                    break
                path.append(i)
                backtrack(res, path, i + 1, k, n)
                path.pop()

        res, path = [], []
        backtrack(res, path, 1, k, n)
        return res


if __name__ == '__main__':
    print(Solution().combinationSum3(k=2, n=6))
