# -*- coding: utf-8 -*-
# @Time    : 2021/9/13 10:59
# @File    : 49. 字母异位词分组.py
from leetcode import *


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for each in strs:
            tmp = ''
            count = collections.Counter(each)
            for key in sorted(count.keys()):
                tmp += key + str(count[key])
            dic[tmp].append(each)
        return list(dic.values())


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = collections.defaultdict(list)
        for each in strs:
            tmp = "".join(sorted(each))
            dic[tmp].append(each)
        return list(dic.values())
