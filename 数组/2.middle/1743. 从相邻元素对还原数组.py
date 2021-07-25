# -*- coding: utf-8 -*-
# @Time    : 2021/07/25 23:11
# @File    : 1743. 从相邻元素对还原数组
from leetcode import *


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        dic = defaultdict(set)
        for x, y in adjacentPairs:
            dic[x].add(y)
            dic[y].add(x)
        start = None
        for key in dic.keys():
            if len(dic[key]) == 1:
                start = key
                break
        key = start
        ans = [key]
        tmp = set(ans)
        total = len(dic.keys())
        while len(ans) != total:
            val = dic[key].pop()
            if val in tmp:
                continue
            ans.append(val)
            tmp.add(val)
            key = val
        return ans


if __name__ == '__main__':
    adjacentPairs = [[2, 1], [3, 4], [3, 2]]
    print(Solution().restoreArray(adjacentPairs))
