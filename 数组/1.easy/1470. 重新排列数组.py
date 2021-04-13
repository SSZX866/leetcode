# -*- coding: utf-8 -*-
# @Time    : 2021/3/29 10:30
# @File    : 1470. 重新排列数组.py
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return sum([[nums[i], nums[i+n]] for i in range(n)],[])

if __name__ == '__main__':
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    print(Solution().shuffle(nums,n))