# -*- coding: utf-8 -*-
# @Time    : 2021/6/22 17:20
# @File    : 17. 电话号码的字母组合.py
from leetcode import *


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {}
        for i in range(2, 7):
            dic[str(i)] = [chr(97 + 3 * (i - 2)), chr(97 + 3 * (i - 2) + 1), chr(97 + 3 * (i - 2) + 2)]
        dic['7'] = ['p', 'q', 'r', 's']
        dic['8'] = ['t', 'u', 'v']
        dic['9'] = ['w', 'x', 'y', 'z']
        # print(dic)
        N = len(digits)
        if not N: return []
        ans = []

        def backtrack(path, target):
            if len(path) == N:
                ans.append(''.join(path))
                return
            for i in range(len(dic[digits[target]])):
                # for j in range(len(dic[digits[i]])):
                path.append(dic[digits[target]][i])
                backtrack(path, target + 1)
                path.pop()

        backtrack([], 0)
        return ans


if __name__ == '__main__':
    print(Solution().letterCombinations("23"))
