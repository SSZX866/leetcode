# -*- coding: utf-8 -*-
# @Time    : 2021/4/29 20:04
# @File    : 1588. 所有奇数长度子数组的和.py
from leetcode import *


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        for i in range(1, len(arr) + 1, 2):
            for j in range(len(arr) - i + 1):
                ans += sum(arr[j:i + j])
        return ans


if __name__ == '__main__':
    arr = [1, 4, 2, 5, 3]
    print(Solution().sumOddLengthSubarrays(arr))
