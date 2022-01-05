# -*- coding: utf-8 -*-
# @Time    : 2022/1/5 10:19
# @File    : 1576. 替换所有的问号.py
from leetcode import *


class Solution:
    def modifyString(self, s: str) -> str:
        i, ans = 0, ''
        while i < len(s):
            if s[i] == '?':
                start = i - 1
                while i < len(s) and s[i] == '?':
                    i += 1
                if i < len(s):
                    if start != -1:
                        tmp = 'a'
                        while tmp == s[start] or tmp == s[i]:
                            tmp = chr(ord(tmp) + 1)
                        tmp += chr(ord(tmp) + 1)
                        while tmp[-1] == s[start] or tmp[-1] == s[i]:
                            tmp = tmp[0] + chr(ord(tmp[-1]) + 1)
                        ans += tmp * ((i - start) // 2)
                        if (i - start) % 2 == 0: ans = ans[:-1]
                    else:
                        tmp = 'a'
                        while tmp == s[i]:
                            tmp = chr(ord(tmp) + 1)
                        tmp += chr(ord(tmp) + 1)
                        while tmp[-1] == s[i]:
                            tmp = tmp[0] + chr(ord(tmp[-1]) + 1)
                        ans += tmp * ((i - start) // 2)
                        if (i - start) % 2 == 0: ans = ans[:-1]
                else:
                    if start != -1:
                        tmp = 'a'
                        while tmp == s[start]:
                            tmp = chr(ord(tmp) + 1)
                        tmp += chr(ord(tmp) + 1)
                        while tmp[-1] == s[start]:
                            tmp = tmp[0] + chr(ord(tmp[-1]) + 1)
                        ans += tmp * ((i - start) // 2)
                        if (i - start) % 2 == 0: ans = ans[:-1]
                    else:
                        tmp = 'ab'
                        ans += tmp * ((i - start) // 2)
                        if (i - start) % 2 == 0: ans = ans[:-1]
            else:
                ans += s[i]
                i += 1

        return ans

if __name__ == '__main__':
    print(Solution().modifyString("b?a"))
