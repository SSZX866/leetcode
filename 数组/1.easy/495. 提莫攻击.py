# -*- coding: utf-8 -*-
# @Time    : 2021/11/10 08:58
# @File    : 495. 提莫攻击.py
from leetcode import *


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        return sum(min(timeSeries[i] - timeSeries[i - 1], duration) for i in range(1, len(timeSeries))) + duration
