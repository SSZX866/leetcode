# -*- coding: utf-8 -*-
# @Time    : 2021/12/10 09:28
# @File    : 748. 最短补全词.py
from leetcode import *


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        target = ""
        for c in licensePlate:
            if c == ' ' or '0' <= c <= '9':
                continue
            if 'A' <= c <= 'Z':
                target += chr(ord(c) + ord('a') - ord('A'))
            else:
                target += c
        licensePlate = target
        words.sort(key=len)
        cnt = collections.Counter(licensePlate)
        for word in words:
            cnt1 = collections.Counter(word)
            flag = False
            for k in cnt:
                if cnt[k] > cnt1[k]:
                    flag = True
                    break
            if flag: continue
            return word
