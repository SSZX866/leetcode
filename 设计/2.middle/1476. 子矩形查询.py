# -*- coding: utf-8 -*-
# @Time    : 2021/4/21 23:26
# @File    : 1476. 子矩形查询.py
from leetcode import *


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.Array = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                self.Array[row][col] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.Array[row][col]


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle
        self.his = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.his.append([row1, col1, row2, col2, newValue])

    def getValue(self, row: int, col: int) -> int:
        for i in range(len(self.his) - 1, -1, -1):
            if self.his[i][0] <= row <= self.his[i][2] and self.his[i][1] <= col <= self.his[i][3]:
                return self.his[i][4]
        return self.rectangle[row][col]
