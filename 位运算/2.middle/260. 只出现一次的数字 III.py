# -*- coding: utf-8 -*-
# @Time    : 2021/10/30 13:06
# @File    : 260. 只出现一次的数字 III.py
from leetcode import *


# 集合 o(n) o(n)
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = set()
        for num in nums:
            if num not in ans:
                ans.add(num)
            else:
                ans.remove(num)
        return list(ans)


# 位运算 o(n) o(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bit = 0
        for num in nums:
            bit ^= num

        # 第k位为1 表示a,b两数第k位不同，区分出两组进行异或
        k = -1
        for i in range(32):
            if (bit >> i) & 1:
                k = i
                break
        a, b = 0, 0
        for num in nums:
            if (num >> k) & 1:
                a ^= num
            else:
                b ^= num
        return [a, b]
