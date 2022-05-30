# -*- coding: utf-8 -*-
# @Time    : 2021/9/12 10:02
# @File    : 678. 有效的括号字符串.py
from leetcode import *


# 贪心 wa 没有考虑 *(这种情况
class Solution:
    def checkValidString(self, s: str) -> bool:
        cnt, delta = 0, 0
        for c in s:
            if c == '*':
                delta += 1
            elif c == '(':
                cnt += 1
            else:
                if cnt:
                    cnt -= 1
                elif delta:
                    delta -= 1
                else:
                    return False
        return delta >= cnt
#
class Solution:
    def checkValidString(self, s: str) -> bool:
        cnt, delta = 0, 0
        for c in s:
            if c == '*':
                delta += 1
            elif c == '(':
                cnt += 1
            else:
                if cnt:
                    cnt -= 1
                elif delta:
                    delta -= 1
                else:
                    return False
        if not delta >= cnt: return False
        cnt, delta = 0, 0
        for c in s[::-1]:
            if c == '*':
                delta += 1
            elif c == ')':
                cnt += 1
            else:
                if cnt:
                    cnt -= 1
                elif delta:
                    delta -= 1
                else:
                    return False
        return delta >= cnt

class Solution:
    def checkValidString(self, s: str) -> bool:
        left, delta = [], []
        for i in range(len(s)):
            if s[i] == '*':
                delta.append(i)
            elif s[i] == '(':
                left.append(i)
            else:
                if left:
                    left.pop()
                elif delta:
                    delta.pop()
                else:
                    return False
        # 排除 *( 的情况
        while left and delta:
            if left.pop() > delta.pop():
                return False
        return not left


# o(n!)
class Solution:
    def __init__(self):
        self.ans = False

    def checkValidString(self, s: str) -> bool:
        n = len(s)

        @lru_cache(None)
        def dfs(left, i):
            if self.ans: return
            if i == n:
                self.ans = not left
                return
            if s[i] == '(':
                dfs(left + 1, i + 1)
            elif s[i] == ')':
                if not left: return
                dfs(left - 1, i + 1)
            else:
                dfs(left + 1, i + 1)
                dfs(left, i + 1)
                if left: dfs(left - 1, i + 1)

        dfs(0, 0)
        return self.ans


if __name__ == '__main__':
    s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
    # s = "(******)))(()()***()))*(())"
    print(Solution().checkValidString(s))
