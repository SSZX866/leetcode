# -*- coding: utf-8 -*-
# @Time    : 2021/07/31 20:19
# @File    : 567. 字符串的排列
from leetcode import *


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        delta = len(s2) - len(s1)
        if delta < 0: return False
        counter = Counter(s1)

        def check(dic):
            for key in counter.keys():
                if counter[key] != dic[key]:
                    return False
            return True

        for i in range(delta + 1):
            if check(Counter(s2[i:i + len(s1)])):
                return True
        return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        delta = len(s2) - len(s1)
        if delta < 0: return False
        counter = Counter(s1)

        def check(dic):
            for key in counter.keys():
                if counter[key] != dic[key]:
                    return False
            return True

        dic = defaultdict(int)
        cnt = Counter(s2[:len(s1)])
        for key in cnt:
            dic[key] = cnt[key]
        if check(cnt): return True

        for i in range(1, delta + 1):
            dic[s2[i - 1]] -= 1
            dic[s2[i + len(s1) - 1]] += 1
            if check(dic):
                return True
        return False
