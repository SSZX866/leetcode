# -*- coding: utf-8 -*-
# @Time    : 2021/5/12 13:56
# @File    : 1190. 反转每对括号间的子串.py
from leetcode import *


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack, ans, i, n = [], "", 0, len(s)
        while i < n:
            if s[i] == '(':
                stack = [""]
                s1, s2, cnt = '', '', 1
                i += 1
                while stack:
                    print(stack, s1, ans)
                    if s[i] == '(':
                        cnt += 1
                        stack.append("")
                    elif s[i] == ')':
                        cnt -= 1
                        tmp = stack.pop()
                        if tmp:
                            if cnt % 2: tmp = tmp[::-1]
                            tmp = tmp.split('|')
                            if len(tmp) > 1:
                                s1 = tmp[0] + s1 + tmp[-1]
                            else:
                                s1 = tmp[0] + s1 if cnt % 2 else s1 + tmp[0]
                            if stack and stack[-1]:
                                stack[-1] += '|'
                    else:
                        stack[-1] += s[i]
                    i += 1
                ans += s1[::-1]
            else:
                ans += s[i] if s[i] != ')' else ''
                i += 1
        return ans


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack, tmp = [], []
        for c in s:
            if c != ')':
                stack.append(c)
            else:
                while stack[-1] != '(':
                    tmp.append(stack.pop())
                stack.pop()
                stack.extend(tmp)
                tmp = []
        return ''.join(stack)


if __name__ == '__main__':
    s = "(ed(et(oc))el)"
    s = "ta()usw((((a))))"
    s = "sxmdll(q)eki(xa)"
    s = "n(ev(t)((()lfevf))yd)cb()"
    s = "v()jhcre((xeplp)wahw(dhgk()qz))"
    "xeplp dhgkqz whaw"
    "dhgkqz whaw xeplp"
    print(Solution().reverseParentheses(s))
