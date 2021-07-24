# -*- coding: utf-8 -*-
# @Time    : 2021/07/24 17:33
# @File    : 剑指 Offer 04. 二维数组中的查找
from leetcode import *


# o(nlogn) 二分+遍历
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        for each_line in matrix:
            lo, hi = 0, len(matrix[0])
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if each_line[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            if lo < len(matrix[0]) and each_line[lo] == target:
                return True
        return False


# o(m+n)从右上角开始找，左边的都小于该值，下边的都大于该值,类似于二分查找树
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        x, y = 0, len(matrix[0]) - 1
        while x < len(matrix) and y >= 0:
            if matrix[x][y] > target:
                y -= 1
            elif matrix[x][y] < target:
                x += 1
            else:
                return True
        return False


if __name__ == '__main__':
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target = 5
    print(Solution().findNumberIn2DArray(matrix, target))
