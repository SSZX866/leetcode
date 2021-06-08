# -*- coding: utf-8 -*-
# @Time    : 2021/6/6 10:58
# @File    : 5778. 使二进制字符串字符交替的最少反转次数.py
from leetcode import *


class Solution:
    def minFlips(self, s: str) -> int:
        dp01left = [0] * len(s)
        dp10left = [0] * len(s)
        dp01right = [0] * len(s)
        dp10right = [0] * len(s)

        dp01left[0] = int(s[0] == '1')
        dp10left[0] = int(s[0] == '0')
        dp01right[0] = int(s[-1] == '0')
        dp10right[0] = int(s[-1] == '1')

        for i in range(1, len(s)):
            dp01left[i] = dp01left[i - 1] + int(s[i] != str(i % 2))
            dp10left[i] = dp10left[i - 1] + int(s[i] == str(i % 2))
            dp01right[i] = dp01right[i - 1] + int(s[-i - 1] == str(i % 2))
            dp10right[i] = dp10right[i - 1] + int(s[-i - 1] != str(i % 2))

        ans = min(dp01left[-1], dp10left[-1], dp10right[-1], dp01right[-1])

        for sep in range(len(s) - 1):
            ans = min(dp01left[sep] + dp01right[len(s) - sep - 2], ans)
            ans = min(dp10left[sep] + dp10right[len(s) - sep - 2], ans)

        # print(dp01left, dp10left, dp10right, dp01right)

        return ans


if __name__ == '__main__':
    s = "10010011010"
    s = "010"
    s = "01001001101"
    print(Solution().minFlips(s))
