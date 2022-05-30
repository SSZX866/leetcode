# -*- coding: utf-8 -*-
# @Time    : 2021/11/29 09:24
# @File    : 438. 找到字符串中所有字母异位词.py
from leetcode import *


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic = {c: 0 for c in p}
        counter = collections.Counter(p)
        n, ans = len(p), []
        left = 0
        for right in range(len(s)):
            if s[right] in dic:
                dic[s[right]] += 1
                while dic[s[right]] > counter[s[right]]:
                    dic[s[left]] -= 1
                    left += 1
                if right - left == n - 1:
                    ans.append(left)
            else:
                while left != right:
                    dic[s[left]] -= 1
                    left += 1
                left += 1
        return ans
