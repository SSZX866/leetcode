# -*- coding: utf-8 -*-
# @Time    : 2021/07/29 12:17
# @File    : 118. 杨辉三角
from leetcode import *


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(2, numRows + 1):
            ans.append([])
            for j in range(i):
                if j == 0 or j == i - 1:
                    ans[-1].append(1)
                else:
                    ans[-1].append(ans[-2][j - 1] + ans[-2][j])
        return ans


if __name__ == '__main__':
    print(Solution().generate(5))
