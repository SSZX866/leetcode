# -*- coding: utf-8 -*-
# @Time    : 2021/6/19 15:03
# @File    : 1000082. 下载插件.py
from leetcode import *


# dp[i][0]
class Solution:
    def leastMinutes(self, n: int) -> int:
        init = 1
        ans = []
        cnt = 0
        while init <= n:
            ans.append(cnt + math.ceil(n / init))
            init *= 2
            cnt += 1

        return min(ans)


if __name__ == '__main__':
    print(Solution().leastMinutes(3))
