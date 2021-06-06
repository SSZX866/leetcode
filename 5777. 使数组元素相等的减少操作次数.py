# -*- coding: utf-8 -*-
# @Time    : 2021/6/6 10:37
# @File    : 5777. 使数组元素相等的减少操作次数.py
from leetcode import *


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        heap = [(-nums[i], i) for i in range(len(nums))]
        heapq.heapify(heap)
        ans = 0
        tmpSet = set(nums)
        while len(tmpSet) > 1:
            tmp = heapq.heappop(heap)


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        ans, i, j, n = 0, 0, 0, len(nums)
        nums.sort(reverse=True)
        # print(nums)
        while j < n:
            while j < n and nums[j] == nums[i]:
                j += 1
            if j == n: break
            ans += j
            # print(nums[i],nums[j],j,i)
            i = j
        if nums[j - 1] != nums[i]: ans += j
        return ans


if __name__ == '__main__':
    nums = [1, 1, 2, 2, 3]
    print(Solution().reductionOperations(nums))
