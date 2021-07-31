# -*- coding: utf-8 -*-
# @Time    : 2021/07/31 21:01
# @File    : 383. 赎金信
from leetcode import *


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt1, cnt2 = Counter(ransomNote), Counter(magazine)
        for key in cnt1:
            if key not in cnt2 or cnt1[key] > cnt2[key]:
                return False
        return True


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(len(ransomNote)):
            if ransomNote[i] in magazine:
                magazine = magazine.replace(ransomNote[i], '', 1)
            else:
                return False
        return True
