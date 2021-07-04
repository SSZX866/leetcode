# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 15:18
# @File    : 645. 错误的集合.py
from leetcode import *


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = [list({i + 1 for i in range(len(nums))} - set(nums))[0]]
        counter = Counter(nums)
        for key in counter.keys():
            if counter[key] == 2:
                ans.append(key)
                return ans[::-1]


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        tmp = {i + 1 for i in range(len(nums))}
        tmp1 = set(nums)
        # return [(sum(nums) - sum(tmp1)), list(tmp - tmp1)[0]]
        # return [(sum(nums) - sum(tmp1)), sum(tmp) - sum(tmp1)]
        return [(sum(nums) - sum(tmp1)), ((len(nums)+1)*len(nums))//2 - sum(tmp1)]


if __name__ == '__main__':
    nums = [1, 2, 2, 4]
    print(Solution().findErrorNums(nums))
