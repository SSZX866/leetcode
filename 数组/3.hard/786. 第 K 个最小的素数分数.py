# -*- coding: utf-8 -*-
# @Time    : 2021/11/29 09:22
# @File    : 786. 第 K 个最小的素数分数.py
from leetcode import *


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        tmp = [(i, j, arr[i] / arr[j]) for j in range(len(arr)) for i in range(j)]
        tmp.sort(key=lambda x: x[2])
        return [arr[tmp[k - 1][0]], arr[tmp[k - 1][1]]]
