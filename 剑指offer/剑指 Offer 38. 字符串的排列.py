# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 11:54
# @File    : 剑指 Offer 38. 字符串的排列.py
from leetcode import *
import time


# 13.217151165008545
class Solution:
    def permutation(self, s: str) -> List[str]:
        def trackback(path, res, s):
            if len(path) == len(s) and path not in res:
                res.append(path)
                return
            for char in s:
                if not path or (path and path.count(char) < s.count(char)):
                    path += char
                    trackback(path, res, s)
                    path = path[:-1]

        res = []
        trackback('', res, s)
        return res


class Solution:
    def permutation(self, s: str) -> List[str]:
        def trackback(path, res, s, n, length):
            if len(path) == length and path not in res:
                res.append(path)
                return
            for i in range(n):
                path += s[i]
                trackback(path, res, s[:i] + s[i + 1:], n - 1, length)
                path = path[:-1]

        res = []
        process = []
        for i, char in enumerate(s):
            if char not in process:
                new_s = s[:i] + s[i + 1:]
                trackback(char, res, new_s, len(new_s), len(new_s) + 1)
            process.append(char)
        return res


class Solution:
    def permutation(self, s: str) -> List[str]:
        def trackback(path, res, s):
            print(path)
            if not s:
                res.append(''.join(path))
                return
            dic = set()
            for i in range(len(s)):
                if s[i] in dic: continue
                dic.add(s[i])
                path.append(s[i])
                new_s = s[0:i] + s[i + 1:]
                trackback(path, res, new_s)
                path.pop()

        res = []
        trackback([], res, s)
        return res


class Solution:
    def permutation(self, s: str) -> List[str]:
        N = len(s)
        ans = set()

        def backtrack(path, stack):
            if len(path) == N:
                ans.add(''.join(path))
                return

            for i in range(N):
                if i in stack:
                    continue
                stack.append(i)
                path.append(s[i])
                backtrack(path, stack)
                stack.pop()
                path.pop()

        backtrack([], [])
        return list(ans)


if __name__ == '__main__':
    s = "abc"
    s = "aab"

    t = time.time()

    print(Solution().permutation(s))
    print(time.time() - t)
