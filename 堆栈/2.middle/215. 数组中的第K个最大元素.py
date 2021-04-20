# -*- coding: utf-8 -*-
# @Time    : 2021/4/20 15:05
# @File    : 215. 数组中的第K个最大元素.py
from leetcode import *

# 小顶堆
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapSmall = []
        for num in nums:
            if k > 0:
                heapq.heappush(heapSmall, num)
                k -= 1
            else:
                if num > heapSmall[0]:
                    heapq.heappop(heapSmall)
                    heapq.heappush(heapSmall, num)

        return heapq.heappop(heapSmall)

# 由于heapq只有小顶堆，故传入(-num,num)使其成为大顶堆(heapq默认按照元组第一个元素排序)
# 对顶堆
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapSmall, heapBig = [], []
        for num in nums:
            if k > 0:
                heapq.heappush(heapSmall, (num, num))
                k -= 1
            else:
                if num > heapSmall[0][1]:
                    tmp = heapq.heappop(heapSmall)[1]
                    heapq.heappush(heapBig, (-tmp, tmp))
                    heapq.heappush(heapSmall, (num, num))
                else:
                    heapq.heappush(heapBig, (-num, num))
            # print(num, heapq.nsmallest(2, heapSmall), heapq.nsmallest(5, heapBig))

        return heapq.heappop(heapSmall)[1]


if __name__ == '__main__':
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(Solution().findKthLargest(nums, k))
