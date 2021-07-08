# -*- coding: utf-8 -*-
# @Time    : 2021/7/8 12:44
# @File    : 930. 和相同的二元子数组.py
from leetcode import *


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # pre = [0]
        # for num in nums:
        #     pre.append(pre[-1] + num)
        pre = [0] + list(accumulate(nums))
        dic = defaultdict(int, {0: 1})
        ans = 0
        for i in range(len(nums)):
            right = pre[i + 1]
            left = right - goal
            ans += dic[left]
            dic[right] += 1
        return ans


if __name__ == '__main__':
    nums = [1, 0, 1, 0, 1]
    goal = 2
    nums = [0, 0, 0, 0, 0]
    goal = 0
    print(Solution().numSubarraysWithSum(nums, goal))
