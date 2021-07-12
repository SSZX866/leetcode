# -*- coding: utf-8 -*-
# @Time    : 2021/4/8 09:44
# @File    : 153. 寻找旋转排序数组中的最小值.py
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j, ans = 0, len(nums) - 1, 5000
        while i <= j:
            mid = (i + j) // 2
            ans = min(ans, nums[i], nums[j], nums[mid])
            if nums[i] <= nums[j]:
                return ans
            elif nums[i] <= nums[mid]:
                i = mid + 1
            else:
                j = mid - 1
        return ans


if __name__ == '__main__':
    nums = [3, 4, 5, 1, 2]
    nums = [4, 5, 6, 7, 0, 1, 2]
    nums = [11, 13, 15, 17]
    nums = [3, 1, 2]
    print(Solution().findMin(nums))
