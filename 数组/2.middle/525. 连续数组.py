# -*- coding: utf-8 -*-
# @Time    : 2021/6/3 21:46
# @File    : 525. 连续数组.py
from leetcode import *


# i = 2*pre[i]   j = 2*pre[j]
# 2*(pre[j]-pre[i]) = j - i
# 2*pre[j] - j = 2*pre[i] - i

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pre, ans = [0], 0
        for i in range(len(nums)):
            pre.append(pre[-1] + nums[i])
            if pre[-1] * 2 == i + 1:
                ans = max(ans, i + 1)

        dic = dict()
        for i in range(len(nums)):
            tmp = 2 * pre[i + 1] - i  # 2*pre[j] - j = 2*pre[i] - i
            if tmp in dic:
                ans = max(ans, i - dic[tmp])
            else:
                dic[tmp] = i  # 取最长的
        return ans


if __name__ == '__main__':
    nums = [1, 1, 1]
    print(Solution().findMaxLength(nums))
