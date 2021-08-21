# -*- coding: utf-8 -*-
# @Time    : 2021/8/21 17:53
# @File    : 209. 长度最小的子数组.py
from leetcode import *

# 713题类似
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 维护一个大于等于target的窗口left，right从0开始
        cur, ans, left = 0, 100001, 0
        for right in range(len(nums)):
            cur += nums[right]
            if cur < target: continue
            while cur >= target:
                ans = min(ans, right - left + 1)
                cur -= nums[left]
                left += 1
        return ans if ans != 100001 else 0
