# -*- coding: utf-8 -*-
# @Time    : 2021/07/29 12:06
# @File    : 557. 反转字符串中的单词 III
from leetcode import *


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([each[::-1] for each in (s.split(' '))])
