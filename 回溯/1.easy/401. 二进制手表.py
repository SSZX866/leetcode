# -*- coding: utf-8 -*-
# @Time    : 2021/6/21 09:56
# @File    : 401. 二进制手表.py
from leetcode import *


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for i in range(12):
            for j in range(60):
                if bin(i).count('1') + bin(j).count('1') == turnedOn:
                    ans.append(str(i) + ':' + str(j)) if j > 9 else ans.append(str(i) + ':0' + str(j))
        return ans


if __name__ == '__main__':
    print(Solution().readBinaryWatch(turnedOn=1))
