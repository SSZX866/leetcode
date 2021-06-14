# -*- coding: utf-8 -*-
# @Time    : 2021/6/13 10:37
# @File    : 5786. 可移除字符的最大数目.py
from leetcode import *


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        lo, hi = 0, len(removable)
        n = len(p)

        def check(index):
            tmp = ''
            j = 0
            comp = removable[:index + 1]
            comp.sort()
            for i in range(len(s)):
                if comp[j] == i:
                    j += 1
                    if j > index:
                        tmp += s[i + 1:]
                        break
                else:
                    tmp += s[i]
            i, j, m = 0, 0, len(tmp)
            while i < m:
                if tmp[i] == p[j]:
                    j += 1
                    if j == n: return True
                i += 1

            return False

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if check(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo


if __name__ == '__main__':
    s = "abcacb"
    p = "ab"
    removable = [3, 1, 0]
    s = "abcbddddd"
    p = "abcd"
    removable = [3, 2, 1, 4, 5, 6]
    print(Solution().maximumRemovals(s, p, removable))
