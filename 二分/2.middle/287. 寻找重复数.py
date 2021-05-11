# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 22:42
# @File    : 287. 寻找重复数.py
from leetcode import *


# 快慢指针
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)

        # def check(target):
        #     return len(set(nums[0:target + 1])) > target

        hi -= 1

        def check(target):
            return sum([1 if x <= target else 0 for x in nums]) <= target

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if check(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo

        # return nums[lo]


if __name__ == '__main__':
    nums = [1, 3, 4, 2, 2]
    nums = [3, 1, 3, 4, 2]
    nums = [1, 1]
    nums = [1, 1, 2]
    print(Solution().findDuplicate(nums))
