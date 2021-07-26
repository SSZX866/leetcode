# -*- coding: utf-8 -*-
# @Time    : 2021/07/24 23:23
# @File    : 5806. 描述绘画结果
from leetcode import *

# 差分数组
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        indices = set()
        line = [0] * 100001
        for start, end, color in segments:
            indices.add(start)
            indices.add(end)
            line[start] += color
            line[end] -= color
        ans = []
        for i in range(1, len(line)):
            line[i] += line[i - 1]
        indices = sorted(indices)
        for i in range(len(indices) - 1):
            if line[indices[i]]:
                ans.append([indices[i], indices[i + 1], line[indices[i]]])
        return ans
