# -*- coding: utf-8 -*-
# @Time    : 2021/9/10 11:28
# @File    : 238. 除自身以外数组的乘积.py
from leetcode import *


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        total = 1
        flag = False
        for num in nums:
            if num == 0 and not flag:
                flag = not flag
                continue
            elif num == 0 and flag:
                return [0] * len(nums)
            total *= num
        for num in nums:
            if not flag:
                ans.append(total // num)
            elif flag:
                if num == 0:
                    ans.append(total)
                else:
                    ans.append(0)
        return ans


# 前缀+后缀数组
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, suf = [1], [1]
        ans = []
        for num in nums:
            pre.append(num * pre[-1])
        for num in nums[::-1]:
            suf.append(num * suf[-1])
        for i in range(len(nums)):
            ans.append(pre[i] * suf[-i - 2])
        return ans
