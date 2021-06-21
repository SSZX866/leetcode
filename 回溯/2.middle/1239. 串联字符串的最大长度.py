# -*- coding: utf-8 -*-
# @Time    : 2021/6/19 15:34
# @File    : 1239. 串联字符串的最大长度.py
from leetcode import *
import copy


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(i, path, ans, helpSet):
            print(path, helpSet)
            if path:
                ans.append("".join(path))

            for each in arr[i:]:
                thisSet = copy.deepcopy(helpSet)
                mark = False
                for char in each:
                    if char in helpSet:
                        mark = True
                        break
                if mark: continue
                for char in each:
                    thisSet.add(char)
                path.append(each)
                backtrack(i + 1, path, ans, thisSet)
                path.pop()

        ans = [""]
        backtrack(0, [], ans, set())
        print(ans)
        return len(max(ans, key=len))


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def validStr(string):
            return len(set(string)) == len(string)

        dp = []
        for s in arr:
            if not validStr(s):
                continue
            for s_ in list(dp):
                if validStr(s_ + s):
                    dp.append(s_ + s)
            dp.append(s)
        return len(max(dp, key=len)) if dp else 0


if __name__ == '__main__':
    arr = ["un", "iq", "ue"]
    print(Solution().maxLength(arr))
