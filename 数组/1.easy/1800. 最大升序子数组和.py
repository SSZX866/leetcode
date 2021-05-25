# -*- coding: utf-8 -*-
# @Time    : 2021/5/24 22:00
# @File    : 1800. 最大升序子数组和.py
import functools

from leetcode import *


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = []
        tmp = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] <= tmp[-1]:
                ans.append(tmp)
                tmp = [nums[i]]
            else:
                tmp.append(nums[i])
        if tmp:
            ans.append(tmp)
        print(ans)
        return max(functools.reduce(lambda x, y: x + y, each) for each in ans)


if __name__ == '__main__':
    nums = [10, 20, 30, 5, 10, 50]
    nums = [3,6,10,1,8,9,9,8,9]
    print(Solution().maxAscendingSum(nums))
