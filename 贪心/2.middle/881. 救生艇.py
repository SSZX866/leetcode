# -*- coding: utf-8 -*-
# @Time    : 2021/8/26 13:08
# @File    : 881. 救生艇.py
from leetcode import *


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        ans = 0
        while left <= right:
            if right - 1 == left:
                ans += 1 if people[left] + people[right] <= limit else 2
                break
            if people[right] + people[right - 1] <= limit:
                ans += 1
                right -= 2
            elif people[right] + people[left] <= limit:
                ans += 1
                left += 1
                right -= 1
            else:
                ans += 1
                right -= 1
        return ans


# 排序后，双指针。如果两人的和小于等于limit，那么左右凑一对儿，往中间递归；否则右边独自占一条船。
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        left, right = 0, n - 1
        ans = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            ans += 1
        return ans
