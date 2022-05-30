# -*- coding: utf-8 -*-
# @Time    : 2021/9/1 10:02
# @File    : 165. 比较版本号.py
from leetcode import *


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = [int(each) for each in version1.split('.')]
        version2 = [int(each) for each in version2.split('.')]
        for i in range(max(len(version1), len(version2))):
            cur1 = 0 if i >= len(version1) else version1[i]
            cur2 = 0 if i >= len(version2) else version2[i]
            if cur1 == cur2: continue
            return 1 if cur1 > cur2 else -1
        return 0
list