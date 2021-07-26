# -*- coding: utf-8 -*-
# @Time    : 2021/7/18 11:00
# @File    : 1937. 扣分后的最大得分.py
from leetcode import *


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        ans = 0
        for pre in range(n):
            tmp_ans = points[0][pre]
            for i in range(1, m):
                j = max(pre - points[i - 1][pre], 0)
                this = j
                while j < min(pre + points[i - 1][pre], n):
                    if points[i][this] - abs(this - pre) < points[i][j] - abs(j - pre):
                        # if points[i][this] - abs(this - pre) <= points[i][j] - abs(j - pre):
                        this = j
                    print(points[i][this], points[i - 1][pre], i)
                    j += 1
                tmp_ans += points[i][this] - abs(pre - this)
                pre = this
                print(tmp_ans)
            ans = max(ans, tmp_ans)
            print('-' * 20)
        return ans


if __name__ == '__main__':
    points = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]
    points = [[0, 3, 0, 4, 2], [5, 4, 2, 4, 1], [5, 0, 0, 5, 1], [2, 0, 1, 0, 3]]
    points = [[1, 5], [3, 2], [4, 2]]
    points = [[0, 0, 4, 1, 4], [2, 1, 2, 0, 1], [2, 2, 1, 3, 4], [5, 2, 4, 5, 4], [0, 5, 4, 2, 5]]
    print(Solution().maxPoints(points))
