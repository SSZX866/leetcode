# -*- coding: utf-8 -*-
# @Time    : 2021/11/1 19:58
# @File    : 720. 词典中最长的单词.py
from leetcode import *
from functools import cmp_to_key


class Solution:
    def longestWord(self, words: List[str]) -> str:
        def my_sort(this, other):
            if len(this) != len(other):
                if max(this, other, key=len) == this:
                    return -1
                return 0
            if min(this, other) == this:
                return -1
            return 0

        tmp = set(words)
        words.sort(key=cmp_to_key(my_sort), reverse=False)
        for word in words:
            flag = True
            for i in range(1, len(word)):
                if word[:i] not in tmp:
                    flag = False
                    break
            if flag: return word
        return ""
