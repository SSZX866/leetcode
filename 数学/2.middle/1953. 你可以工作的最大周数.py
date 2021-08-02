# -*- coding: utf-8 -*-
# @Time    : 2021/08/02 19:42
# @File    : 1953. 你可以工作的最大周数
from leetcode import *


class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        mx = max(milestones)
        total = sum(milestones)
        return total if mx * 2 <= total else (total - mx) * 2 + 1
