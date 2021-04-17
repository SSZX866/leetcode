# -*- coding: utf-8 -*-
# @Time    : 2021/4/17 13:00
# @File    : 219. 存在重复元素 II.py
from leetcode import *


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic, i, n, queue = set(), 0, len(nums), []
        while i < n:
            if i > k:
                dic.remove(queue.pop(0))
            if nums[i] not in dic:
                dic.add(nums[i])
                queue.append(nums[i])
            else:
                return True
            i += 1
        return False


if __name__ == '__main__':
    nums = [4, 1, 2, 3, 1, 5]
    k = 3
    print(Solution().containsNearbyDuplicate(nums, k))
