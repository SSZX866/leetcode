# -*- coding: utf-8 -*-
# @Time    : 2021/3/31 19:14
# @File    : 22. 括号生成.py
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(path, res, n):
            print(path)
            if isValid(path) and len(path) == 2 * n:
                res.append(path[:])
                return
            if len(path) == 2 * n:
                return
            for i in range(2):
                path.append('()'[i])
                backtrack(path, res, n)
                path.pop()

        def isValid(path):
            stack = []
            for p in path:
                if p == '(':
                    stack.append('(')
                else:
                    if stack:
                        stack.pop()
                    else:
                        return False
            if stack:
                return False
            else:
                return True

        path, res, result = [], [], []
        backtrack(path, res, n)
        for i in range(len(res)):
            result.append('')
            for j in res[i]:
                result[i] += j
        return result


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path, left, right):
            if len(path) == 2 * n:
                res.append(''.join(path[:]))
                return
            if left < n:
                path.append('(')
                backtrack(path, left + 1, right)
                path.pop()
            if right < left:
                path.append(")")
                backtrack(path, left, right + 1)
                path.pop()

        backtrack([], 0, 0)
        return res


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def check(target):
            cnt = 0
            for c in target:
                if c == '(':
                    cnt += 1
                else:
                    cnt -= 1
                if cnt < 0: return False
            return True

        def backtrack(path):
            if len(path) == 2 * n:
                ans.append(''.join(path))
                return
            for c in '()':
                path.append(c)
                if not check(path) or path.count('(') > n:
                    path.pop()
                    continue
                backtrack(path)
                path.pop()

        backtrack([])
        return ans


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
