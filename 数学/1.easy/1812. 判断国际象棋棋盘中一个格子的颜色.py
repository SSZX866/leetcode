# -*- coding: utf-8 -*-
# @Time    : 2021/4/3 22:30
# @File    : 1812. 判断国际象棋棋盘中一个格子的颜色.py
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        return (dic[coordinates[0]] + int(coordinates[1])) % 2 == 0
