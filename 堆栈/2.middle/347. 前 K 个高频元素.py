# -*- coding: utf-8 -*-
# @Time    : 2021/4/22 17:44
# @File    : 347. 前 K 个高频元素.py
from leetcode import *
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic, heap = dict(), []
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        for key in dic:
            if len(heap) < k:
                heapq.heappush(heap, (dic[key], key))
            elif len(heap) == k and heap[0][0] < dic[key]:
                heapq.heappush(heap, (dic[key], key))
                heapq.heappop(heap)
        return [x[1] for x in heap]


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(Solution().topKFrequent(nums, k))
