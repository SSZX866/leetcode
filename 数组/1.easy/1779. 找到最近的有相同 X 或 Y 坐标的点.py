# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 11:23
# @File    : 1779. 找到最近的有相同 X 或 Y 坐标的点.py
from leetcode import *


class Help:
    def __init__(self, a, x, y):
        self.val = a
        self.x = x
        self.y = y

    def __lt__(self, other):
        print(self.val, other.val, 11111)
        print(((self.val[0][0] - self.x) ** 2 + (self.val[0][1] - self.y) ** 2 < (other.val[0][0] - other.x) ** 2 + (
                other.val[0][1] - other.y) ** 2) and (self.val[1] < other.val[1]))
        return ((self.val[0][0] - self.x) ** 2 + (self.val[0][1] - self.y) ** 2 < (other.val[0][0] - other.x) ** 2 + (
                other.val[0][1] - other.y) ** 2) and (self.val[1] < other.val[1])


# 重写比较方法 不对
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        tmp = []
        for i, point in enumerate(points):
            if point[0] == x or point[1] == y:
                tmp.append(Help([point, i], x, y))
        if not tmp: return -1
        ans = tmp[0]
        print(ans.val)
        for each in tmp[1:]:
            ans = each if each < ans else ans
            print(ans.val)
        return ans.val[0][1]


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        tmp = []
        for i, point in enumerate(points):
            if point[0] == x or point[1] == y:
                tmp.append([point, i])
        if not tmp: return -1
        tmp.sort(key=lambda a: ((a[0][0] - x) ** 2 + (a[0][1] - y) ** 2, a[1]))
        return tmp[0][1]


if __name__ == '__main__':
    x = 3
    y = 4
    points = [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]
    print(Solution().nearestValidPoint(x, y, points))
