# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 22:07
# @File    : 1781. 所有子字符串美丽值之和.py
from leetcode import *


class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        ans = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                tmpCounter = Counter(s[i:j+1])
                ans[i][j] = tmpCounter[max(tmpCounter, key=lambda x: tmpCounter[x])] - tmpCounter[
                    min(tmpCounter, key=lambda x: tmpCounter[x])]
        #         print(ans[i][j], tmpCounter,s[i:j])
        # print(ans)
        return sum([sum(each) for each in ans])


if __name__ == '__main__':
    s = "aabcb"
    print(Solution().beautySum(s))
