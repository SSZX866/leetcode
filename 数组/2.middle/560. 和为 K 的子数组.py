# -*- coding: utf-8 -*-
# @Time    : 2021/9/10 11:41
# @File    : 560. 和为 K 的子数组.py
from leetcode import *


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0]
        for num in nums:
            pre.append(pre[-1] + num)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if pre[j] - pre[i] == k:
                    ans += 1
        return ans


# 优化时间o(n) 进阶两数之和
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0]
        for num in nums:
            pre.append(pre[-1] + num)
        ans = 0
        dic = collections.defaultdict(int)
        for i in range(n + 1):
            ans += dic[pre[i] - k]
            dic[pre[i]] += 1
        return ans


# 优化空间o(1)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        pre = 0
        dic = collections.defaultdict(int)
        dic[0] = 1  # 初始加入左边界
        for i in range(len(nums)):
            pre += nums[i]
            ans += dic[pre - k]
            dic[pre] += 1
        return ans
