# -*- coding: utf-8 -*-
# @Time    : 2021/8/26 14:27
# @File    : 40. 组合总和 II.py
from leetcode import *


# indexs记录当前使用过的下标，dic记录已存在的答案o(1)查询
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans, dic, indexs = [], set(), set()

        def backtrack(path, curSum):
            if curSum == target:
                ans.append(path[:])
            for i in range(len(candidates)):
                newSum = curSum + candidates[i]
                if newSum > target:
                    break
                if i in indexs:
                    continue
                tmp = tuple(sorted(path + [candidates[i]]))
                if tmp in dic:
                    continue
                dic.add(tmp)
                indexs.add(i)
                path.append(candidates[i])
                backtrack(path, newSum)
                path.pop()
                indexs.remove(i)

        backtrack([], 0)
        return ans
