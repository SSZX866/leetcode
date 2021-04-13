# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 15:26
# @File    : 6. Z 字形变换.py
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = [[] for _ in range(numRows)]
        index, flag = 0, True
        for c in s:
            ans[index].append(c)
            index = (index + 1) % (numRows) if flag else (index - 1) % (numRows)
            if index == 0 or index == numRows - 1: flag = not flag
        return ''.join([''.join(a) for a in ans])


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    s = "PAYPALISHIRING"
    numRows = 4
    print(Solution().convert(s, numRows))
