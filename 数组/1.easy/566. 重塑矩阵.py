# -*- coding: utf-8 -*-
# @Time    : 2021/07/29 12:07
# @File    : 566. 重塑矩阵
from leetcode import *


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat[0]) * len(mat): return mat
        source = [each for line in mat for each in line]
        ans = [[]]
        for num in source:
            if len(ans[-1]) < c:
                ans[-1].append(num)
            if len(ans[-1]) == c and len(ans) < r:
                ans.append([])
        return ans

# 坐标变换
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums

        ans = [[0] * c for _ in range(r)]
        for x in range(m * n):
            ans[x // c][x % c] = nums[x // n][x % n]

        return ans
