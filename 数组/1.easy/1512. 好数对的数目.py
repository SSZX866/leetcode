# -*- coding: utf-8 -*-
# @Time    : 2021/3/29 10:14
# @File    : 1512. 好数对的数目.py
from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        calc = []
        for num in set(nums):
            if nums.count(num) > 1:
                calc.append(nums.count(num))
        return sum(sum(range(n)) for n in calc)

if __name__ == '__main__':
    nums = [1, 2, 3, 1, 1, 3]
    print(Solution().numIdenticalPairs(nums))