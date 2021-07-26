# -*- coding: utf-8 -*-
# @Time    : 2021/07/26 10:51
# @File    : 1713. 得到子序列的最少操作次数
from leetcode import *


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        hashmap = defaultdict(list)
        for i in range(len(arr) - 1, -1, -1):
            hashmap[arr[i]].append(i)
        indices = []
        for s in target:
            indices += hashmap[s]
        result = []
        for index in indices:
            insert_index = bisect.bisect_left(result, index)
            if insert_index == len(result):
                result.append(index)
            else:
                result[insert_index] = index
        return len(target) - len(result)
