# -*- coding: utf-8 -*-
# @Time    : 2021/4/17 11:51
# @File    : 220. 存在重复元素 III.py
from leetcode import *


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        i, dic, n, queue = 0, {}, len(nums), []
        while i < n:
            if i > k:
                dic.pop(queue.pop(0))
            bucket = nums[i] // (t + 1)
            if bucket not in dic:
                if bucket - 1 in dic and abs(nums[i] - dic[bucket - 1]) <= t: return True
                if bucket + 1 in dic and abs(dic[bucket + 1] - nums[i]) <= t: return True
                dic[bucket] = nums[i]
                queue.append(bucket)
            else:
                return True
            i += 1
            # print(dic)
        return False


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    k = 3
    t = 0

    nums = [1, 0, 1, 1]
    k = 1
    t = 2

    nums = [1, 5, 9, 1, 5, 9]
    k = 2
    t = 3
    print(Solution().containsNearbyAlmostDuplicate(nums, k, t))
