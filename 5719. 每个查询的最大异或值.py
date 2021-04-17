# -*- coding: utf-8 -*-
# @Time    : 2021/4/17 22:43
# @File    : 5719. 每个查询的最大异或值.py
from leetcode import *


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans, pre, maximum, xor = [], None, pow(2, maximumBit), int('0b' + '1' * maximumBit, 2)
        for num in nums:
            if pre == None:
                pre = num
            else:
                pre = pre ^ num
            res = pre ^ xor
            print(pre, bin(pre), res, bin(res))
            if res >= maximum:
                res = res << 1
            ans = [res] + ans
        return ans


if __name__ == '__main__':
    nums = [0, 1, 1, 3]
    maximumBit = 2
    nums = [2, 3, 4, 7]
    maximumBit = 3
    print(Solution().getMaximumXor(nums, maximumBit))
