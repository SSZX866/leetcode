# -*- coding: utf-8 -*-
# @Time    : 2021/6/22 16:05
# @File    : 394. 字符串解码.py
from leetcode import *

# 递归
class Solution:
    def decodeString(self, s: str) -> str:
        ans = ''
        i = 0
        N = len(s)
        while i < N:
            total = ''
            while i < N and s[i] != '[':
                if s[i] in '0123456789':
                    total += s[i]
                    i += 1
                    continue
                ans += s[i]
                i += 1
            if i < N:
                i += 1
                tmp = ''
                cnt = 1
                while cnt:
                    if s[i] == '[':
                        cnt += 1
                    if s[i] == ']':
                        cnt -= 1
                    if cnt: tmp += s[i]
                    i += 1
                ans += int(total) * self.decodeString(tmp)
        return ans

# 栈
class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        # stack = [下一次的数量，'上一次的结果']
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)
            else:
                res += c
            print(stack,res)
        return res


if __name__ == '__main__':
    s = "3[a]2[bc]"
    s = "3[a2[c]]"
    print(Solution().decodeString(s))
