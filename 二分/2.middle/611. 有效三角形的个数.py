# -*- coding: utf-8 -*-
# @Time    : 2021/08/04 10:23
# @File    : 611. 有效三角形的个数
from leetcode import *


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        # 固定最大边, a + b > c
        for i in range(n - 1, 1, -1):
            l, r = 0, i - 1
            # 两数之和问题！
            while l < r:
                # 两数之和大于最大边，他们之间的所有值作为左端点，均可以和右端点构成答案
                if nums[l] + nums[r] > nums[i]:
                    ans += r - l
                    r -= 1
                else:
                    # 小于最大边，构不成答案，之后的右端点都需要更大的左端点才有可能继续构成答案
                    l += 1
        return ans


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                left, right, k = j + 1, n - 1, j
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] < nums[i] + nums[j]:
                        k = mid
                        left = mid + 1
                    else:
                        right = mid - 1
                ans += k - j
        return ans
