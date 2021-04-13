# -*- coding: utf-8 -*-
# @Time    : 2021/4/2 15:49
# @File    : 51. N 皇后.py
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(res, path, n):
            if len(path) == n:
                res.append(path[:])
            for i in range(n):
                if isValid(path, i):
                    path.append(i)
                    backtrack(res, path, n)
                    path.pop()

        def isValid(path, i):
            if not path:
                return True
            elif i not in path:
                length = len(path)
                for index in range(length):
                    if path[index] - index == i - length:
                        return False
                    if path[index] + index == i + length:
                        return False
                return True
            else:
                return False

        res = []
        backtrack(res, [], n)
        result = []
        for each in res:
            result.append(['.' * x + 'Q' + '.' * (len(each) - x - 1) for x in each])
        return result


if __name__ == '__main__':
    print(Solution().solveNQueens(4))
