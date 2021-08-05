# -*- coding: utf-8 -*-
# @Time    : 2021/08/05 12:16
# @File    : 784. 字母大小写全排列
from leetcode import *


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []

        def backtrack(path, target):
            if len(path) == len(s):
                ans.append(''.join(path))
                return
            for i in range(len(target)):
                if target[i].isdigit():
                    path.append(target[i])
                    backtrack(path, target[i + 1:])
                    path.pop()
                    continue
                path.append(target[i].capitalize())
                backtrack(path, target[i + 1:])
                path.pop()
                path.append(target[i].lower())
                backtrack(path, target[i + 1:])
                path.pop()

        backtrack([], s)
        return ans
