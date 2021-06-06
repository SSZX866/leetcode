# -*- coding: utf-8 -*-
# @Time    : 2021/6/6 10:33
# @File    : 5776. 判断矩阵经轮转后是否一致.py
from leetcode import *


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        ans = [mat]
        for i in range(3):
            ans.append([list(each[::-1]) for each in zip(*ans[-1])])
        print(ans)
        return target in ans
if __name__ == '__main__':
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    target = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
    print(Solution().findRotation(mat,target))