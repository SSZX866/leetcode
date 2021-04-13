# -*- coding: utf-8 -*-
# @Time    : 2021/3/29 13:20
# @File    : 1486. 数组异或操作.py
from typing import List

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result, nums = 0, list(map(lambda x: (2*x+start), range(n)))
        for i in range(n):
            result = result^nums[i]
        return result
if __name__ == '__main__':
    print(Solution().xorOperation(10,5))