# -*- coding: utf-8 -*-
# @Time    : 2021/4/21 23:17
# @File    : 1119. 删去字符串中的元音.py
from leetcode import *


class Solution:
    def removeVowels(self, s: str) -> str:
        return s.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')


if __name__ == '__main__':
    print(Solution().removeVowels('aeiou'))
