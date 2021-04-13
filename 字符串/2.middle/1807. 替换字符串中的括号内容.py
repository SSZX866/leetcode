# -*- coding: utf-8 -*-
# @Time    : 2021/3/28 10:47
# @File    : 5714. 替换字符串中的括号内容.py

from typing import List


class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        n, i, j, result, know = len(s), 0, 0, '', {}
        for each in knowledge:
            know[each[0]] = each[1]
        while i < n:
            j = i
            if s[i] == '(':
                i += 1
                while s[j] != ')':
                    j += 1
                if s[i:j] in know:
                    result += know[s[i:j]]
                else:
                    print(s[i:j])
                    result += '?'
                i = j
            else:
                result += s[i]
            i += 1
        return result


if __name__ == '__main__':
    s = "(name)isyea(age)rsold(age)(age)"
    knowledge = [["name", "bob"], ["age", "two"]]
    print(Solution().evaluate(s, knowledge))
