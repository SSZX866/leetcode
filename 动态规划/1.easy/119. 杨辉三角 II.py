# -*- coding: utf-8 -*-
# @Time    : 2021/08/06 12:56
# @File    : 119. 杨辉三角 II
from leetcode import *


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        while rowIndex:
            tmp = []
            for i in range(len(ans) + 1):
                if i == 0 or i == len(ans):
                    tmp.append(1)
                else:
                    tmp.append(ans[i] + ans[i - 1])
            ans = tmp
            rowIndex -= 1
        return ans
