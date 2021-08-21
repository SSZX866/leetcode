# -*- coding: utf-8 -*-
# @Time    : 2021/8/21 17:05
# @File    : 438. 找到字符串中所有字母异位词.py
from leetcode import *


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p): return []
        target = Counter(p)
        dic = defaultdict(int)
        ans = []
        for i in range(len(s)):
            dic[s[i]] += 1
            if i >= len(p) - 1:
                if target == dic:
                    ans.append(i - len(p) + 1)
                dic[s[i - len(p) + 1]] -= 1
                if dic[s[i - len(p) + 1]] == 0:
                    del dic[s[i - len(p) + 1]]
        return ans
