# -*- coding: utf-8 -*-
# @Time    : 2021/6/2 09:51
# @File    : 523. 连续的子数组和.py
from leetcode import *


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre = [0]
        for num in nums:
            pre.append(num + pre[-1])
        dic = {}
        for i in range(len(nums) + 1):
            if pre[i] % k in dic and i - dic[pre[i] % k] > 1: return True
            if pre[i] % k not in dic: dic[pre[i] % k] = i
            print(dic)
        return False


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        modes = set()
        presum = 0
        for num in nums:
            last = presum
            # 当前前缀和
            presum += num
            presum %= k
            # 同余定理
            if presum in modes:
                return True
            # 上一个前缀和，下一个就可以用了（距离为2了）
            modes.add(last)
        return False


if __name__ == '__main__':
    nums = [23, 2, 4, 6, 7]
    k = 6
    nums = [23, 2, 4, 6, 6]
    k = 7
    nums = [5, 0, 0, 0]
    k = 3
    print(Solution().checkSubarraySum(nums, k))
