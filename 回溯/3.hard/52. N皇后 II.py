# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 19:30
# @File    : 52. N皇后 II.py
class Solution:
    def totalNQueens(self, n: int) -> int:
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
        print(res)
        return len(res)


if __name__ == '__main__':
    print(Solution().totalNQueens(4))
