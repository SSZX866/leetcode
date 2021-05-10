# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 22:41
# @File    : 5732. 减小和重新排列数组后的最大元素.py
from leetcode import *


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        ans = [1]
        for a in arr[1:]:
            pre = ans[-1]
            if a > pre:
                ans.append(pre + 1)
            elif a == pre:
                ans.append(pre)
        return ans[-1]


if __name__ == '__main__':
    arr = [[2, 2, 1, 2, 1], [100, 1, 1000], [1, 2, 3, 4, 5]]
    for a in arr:
        print(Solution().maximumElementAfterDecrementingAndRearranging(a))
