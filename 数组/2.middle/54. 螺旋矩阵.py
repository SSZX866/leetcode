# -*- coding: utf-8 -*-
# @Time    : 2021/3/15 9:26
# @File    : 54. 螺旋矩阵.py
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        n, m = len(matrix), len(matrix[0])
        boundary = [[0, 0], [n - 1, m - 1]]
        face = 1  # 0,1,2,3 分别代表北东南西
        result = []
        i, j = 0, 0
        for _ in range(n * m):
            # 更新face
            if i > boundary[1][0] or j > boundary[1][1] or i < boundary[0][0] or j < boundary[0][1]:
                # print(i,j,boundary)
                face = (face + 1) % 4
                # 更新boundary, 纠正i,j
                if face == 0:
                    boundary[1][0] -= 1
                    j += 1
                    i -= 1
                elif face == 1:
                    boundary[0][1] += 1
                    i += 1
                    j += 1
                elif face == 2:
                    boundary[0][0] += 1
                    j -= 1
                    i += 1
                else:
                    boundary[1][1] -= 1
                    i -= 1
                    j -= 1
            # print(i, j, face, result,boundary)
            result.append(matrix[i][j])
            # 更新i, j
            if face == 0:
                i -= 1
            elif face == 1:
                j += 1
            elif face == 2:
                i += 1
            else:
                j -= 1
        return result


# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         res = []
#         while matrix:
#             res += matrix.pop(0)
#             matrix = list(zip(*matrix))[::-1]
#         return res

if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(Solution().spiralOrder(matrix))
