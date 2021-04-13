# -*- coding: utf-8 -*-
# @Time    : 2021/4/1 21:41
# @File    : 1732. 找到最高海拔.py
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0]
        for i in range(len(gain)):
            res.append(gain[i] + res[i])
        return max(res)


if __name__ == '__main__':
    print(Solution().largestAltitude(gain=[-5, 1, 5, 0, -7]))
