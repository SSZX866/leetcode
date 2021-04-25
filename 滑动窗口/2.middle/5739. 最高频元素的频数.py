# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 15:38
# @File    : 5739. 最高频元素的频数.py
from leetcode import *


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        pre = [0]
        for num in nums:
            pre.append(pre[-1] + num)
        left, ans = 0, 1
        for right in range(len(nums)):
            # 维护一个窗口，窗口内元素经过不超过k次操作，可全部变为最右端元素
            while nums[right] * (right - left) - (pre[right] - pre[left]) > k:
                left += 1
            ans = max(ans, right - left + 1)
        # print(pre)
        return ans


# 最大数乘以窗口大小 - 窗口中所有数的和 <= k
# max * size - sum <= k ---> max * size <= k + sum
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        for j in range(len(nums)):
            k += nums[j]
            if nums[j] * (j - i + 1) > k:
                k -= nums[i]
                i += 1
        # 因为已经排序，所以最后记录的情况必是最大的，无需使用max函数
        return j - i + 1


if __name__ == '__main__':
    nums = [1, 2, 4]
    k = 5
    print(Solution().maxFrequency(nums, k))
    nums = [1, 4, 8, 13]
    k = 5
    print(Solution().maxFrequency(nums, k))
