# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 10:33
# @File    : 179. 最大数.py
from typing import List


# 含有子串且母串后一位比前一位大的案例不行 如nums = [34323, 3432]
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(str(max(nums)))
        nums = list(map(str, nums))
        helpers = []
        for num in nums:
            length = len(num)
            helpers.append([num + num[-1] * (n - length), length])
        helpers.sort(key=lambda x: x[0], reverse=True)
        ans = ''
        for helper in helpers:
            print(helper)
            ans += helper[0][:helper[1]]
        return ans


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(lambda x, y: 1 if x + y < y + x else -1))
        return ''.join(nums) if nums[0] != '0' else '0'


if __name__ == '__main__':
    nums = [3, 30, 34, 5, 9]
    nums = [1]
    nums = [10, 2]
    nums = [393, 39, 4, 5]
    nums = [34323, 3432]
    print(Solution().largestNumber(nums))
