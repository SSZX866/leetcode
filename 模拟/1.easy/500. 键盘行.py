# -*- coding: utf-8 -*-
# @Time    : 2021/11/1 09:09
# @File    : 500. 键盘行.py
from leetcode import *


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dics = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        ans = []
        for word in words:
            for dic in dics:
                if word[0].lower() in dic:
                    flag = True
                    for s in word:
                        if s.lower() not in dic:
                            flag = False
                            break
                    if flag:
                        ans.append(word)
                    else:
                        break
        return ans


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dics = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        ans = []
        for word in words:
            tmp = set(word.lower())
            # 集合比较
            if tmp <= dics[0] or tmp <= dics[1] or tmp <= dics[2]:
                ans.append(word)
        return ans
