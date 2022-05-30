# -*- coding: utf-8 -*-
# @Time    : 2021/12/2 09:05
# @File    : 506. 相对名次.py
from leetcode import *

dic = dict([(1, "Gold Medal"), (2, "Silver Medal"), (3, "Bronze Medal")])


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sort_list = [(i, athlete) for i, athlete in enumerate(score)]
        sort_list.sort(key=lambda x: -x[1])
        rank_list = [(idx, rank + 1) for rank, (idx, _) in enumerate(sort_list)]
        rank_list.sort(key=lambda x: x[0])
        ans = [dic[each] if each in dic else str(each) for _, each in rank_list]
        return ans
