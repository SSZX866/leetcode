# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 14:31
# @File    : 1854. 人口最多的年份.py
from leetcode import *


# 计数
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        tmp = []
        for log in logs:
            tmp += list(range(log[0], log[1]))
        cnt = Counter(tmp)
        ans = [[cnt[key], key] for key in cnt]
        ans.sort(key=lambda x: (x[0], -x[1]))
        return ans[-1][1]


# 差分数组
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        delta, pre = [0] * 101, [0]
        # 差分数组
        for log in logs:
            delta[log[0] - 1950] += 1
            delta[log[1] - 1950] -= 1
        # 前缀和
        for i in range(1, 101):
            pre.append(pre[-1] + delta[i])
        return pre.index(max(pre)) + 1950


if __name__ == '__main__':
    logs = [[1993, 1999], [2000, 2010]]
    logs = [[1950, 1961], [1960, 1971], [1970, 1981]]
    print(Solution().maximumPopulation(logs))
