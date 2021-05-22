# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 15:06
# @File    : 370. 区间加法.py
from leetcode import *

# 差分数组
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        delta = [0] * (length + 1)
        for update in updates:
            delta[update[0]] += update[2]
            delta[update[1] + 1] -= update[2]
        ans = [delta[0]]
        for i in range(1, length):
            ans.append(ans[-1] + delta[i])
        return ans


if __name__ == '__main__':
    length = 5
    updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
    print(Solution().getModifiedArray(length, updates))
