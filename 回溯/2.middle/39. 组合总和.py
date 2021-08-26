# -*- coding: utf-8 -*-
# @Time    : 2021/8/26 14:26
# @File    : 39. 组合总和.py
from leetcode import *


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans, dic = [], set()

        def backtrack(path, curSum):
            if curSum == target:
                ans.append(path[:])
            for candidate in candidates:
                newSum = curSum + candidate
                if newSum > target:
                    break
                tmp = tuple(sorted(path + [candidate]))
                if tmp in dic:
                    continue
                dic.add(tmp)
                path.append(candidate)
                backtrack(path, newSum)
                path.pop()

        backtrack([], 0)
        return ans
