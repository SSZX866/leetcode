# -*- coding: utf-8 -*-
# @Time    : 2021/4/1 10:57
# @File    : 1079. 活字印刷.py
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(res, path, tiles):
            s = ''.join(path[:])
            if path and s not in res:
                res.append(s)
            for i in range(len(tiles)):
                path.append(tiles[i])
                backtrack(res, path, tiles[:i] + tiles[i + 1:])
                path.pop()

        res, path = [], []
        backtrack(res, path, tiles)
        return len(res)


if __name__ == '__main__':
    print(Solution().numTilePossibilities("AAABBCCC"))
