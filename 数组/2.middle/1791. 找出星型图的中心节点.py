# -*- coding: utf-8 -*-
# @Time    : 2021/5/27 10:11
# @File    : 1791. 找出星型图的中心节点.py
from leetcode import *


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        tmp = list(zip(*edges))
        cnt = Counter(tmp[0]) + Counter(tmp[1])
        return max(cnt, key=lambda x: cnt[x])
