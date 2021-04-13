# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 13:17
# @File    : 1281. 整数的各位积和之差.py
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = list(map(int, str(n)))
        multi = 1
        for i in range(len(nums)):
            multi *= nums[i]
        return multi - sum(nums)
