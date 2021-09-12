# -*- coding: utf-8 -*-
# @Time    : 2021/9/12 13:04
# @File    : 763. 划分字母区间.py
from leetcode import *


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = defaultdict(lambda: [1000, -1])  # [最早出现下标，最晚出现下标]
        for i in range(len(s)):
            dic[s[i]][0] = min(dic[s[i]][0], i)
            dic[s[i]][1] = max(dic[s[i]][1], i)
        # 合并重叠区间
        pre = -1
        ans = []
        for start, end in sorted(dic.values(), key=lambda x: (x[0], x[1])):
            if start < pre:
                pre = max(end, pre)
            else:
                ans.append(pre)
                pre = end
        # 前缀和差分
        ans.append(len(s) - ans[-1] - 1)
        for i in range(len(ans) - 2, 0, -1):
            ans[i] -= ans[i - 1]
        return ans[1:]
