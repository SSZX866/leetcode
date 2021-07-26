# -*- coding: utf-8 -*-
# @Time    : 2021/07/26 11:02
# @File    : 1941. 检查是否所有字符出现次数相同
from leetcode import *


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = Counter(s)
        return len(set(counter.values())) == 1
