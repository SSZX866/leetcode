# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 13:28
# @File    : 1861. 旋转盒子.py
from leetcode import *


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        for each in box:
            i = j = n - 1
            while i >= 0:
                while j >= 0 and (each[j] == '*' or each[j] == '#'):
                    j -= 1
                if j == 0: break
                i = j - 1
                while i >= 0 and each[i] != '*':
                    if each[i] == '#':
                        each[j] = '#'
                        each[i] = '.'
                        j -= 1
                    i -= 1
                if i == 0: break
                j = i
        ans = [list(each[::-1]) for each in zip(*box)]
        return ans


if __name__ == '__main__':
    box = [["#", ".", "#"]]
    box = [["#", ".", "*", "."],
           ["#", "#", "*", "."]]
    box = [["#", "#", "*", ".", "*", "."],
           ["#", "#", "#", "*", ".", "."],
           ["#", "#", "#", ".", "#", "."]]

    print(Solution().rotateTheBox(box))
