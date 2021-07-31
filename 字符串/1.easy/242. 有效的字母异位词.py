# -*- coding: utf-8 -*-
# @Time    : 2021/07/31 21:05
# @File    : 242. 有效的字母异位词
from leetcode import *
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt1, cnt2 = Counter(s), Counter(t)
        if sorted(cnt1.keys()) != sorted(cnt2.keys()): return False
        for key in cnt1.keys():
            if cnt1[key] != cnt2[key]:
                return False
        return True