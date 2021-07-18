# -*- coding: utf-8 -*-
# @Time    : 2021/7/18 21:39
# @File    : 面试题 10.02. 变位词组.py
from leetcode import *


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for each in strs:
            dict[''.join(sorted(each))].append(each)
        ans = []
        for key in dict.keys():
            ans.append(dict[key])
        return ans
