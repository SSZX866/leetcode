# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 22:48
# @File    : 5781. 删除一个字符串中所有出现的给定子字符串.py
from leetcode import *


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        def KMP_algorithm(string, substring):
            pnext = gen_pnext(substring)
            n = len(string)
            m = len(substring)
            i, j = 0, 0
            while i < n and j < m:
                if string[i] == substring[j]:
                    i += 1
                    j += 1
                elif j != 0:
                    j = pnext[j - 1]
                else:
                    i += 1
            if j == m:
                return i - j
            else:
                return -1

        def gen_pnext(substring):
            index, m = 0, len(substring)
            pnext = [0] * m
            i = 1
            while i < m:
                if substring[i] == substring[index]:
                    pnext[i] = index + 1
                    index += 1
                    i += 1
                elif index != 0:
                    index = pnext[index - 1]
                else:
                    pnext[i] = 0
                    i += 1
            return pnext

        i = KMP_algorithm(s, part)
        N = len(part)
        while i != -1:
            s = s[:i] + s[i + N:]
            i = KMP_algorithm(s, part)

        return s


if __name__ == '__main__':
    s = "daabcbaabcbc"
    part = "abc"
    s = "axxxxyyyyb"
    part = "xy"
    print(Solution().removeOccurrences(s, part))
