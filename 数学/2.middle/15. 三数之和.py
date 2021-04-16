# -*- coding: utf-8 -*-
# @Time    : 2021/4/15 20:03
# @File    : 15. 三数之和.py
from typing import List


# 9940ms
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic, n, ans = {}, len(nums), []
        for i in range(n):
            dic = {}
            for j in range(i + 1, n):
                key = nums[j]
                if key in dic:
                    value = dic[key] + [key]
                    value.sort()
                    if value not in ans:
                        ans.append(value)
                key = -nums[i] - nums[j]
                if key not in dic:
                    dic[key] = [nums[i], nums[j]]
        return ans

# 1156ms
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans, n = [], len(nums) - 1
        for i in range(n - 1):
            if i > 0 and nums[i] == nums[i - 1]: continue
            k = n
            j = i + 1
            while j < k:
                if j > i + 1 and nums[j] == nums[j - 1]:
                    j += 1
                    continue
                while j < k - 1 and nums[i] + nums[j] + nums[k - 1] >= 0:
                    k -= 1
                if nums[i] + nums[j] + nums[k] == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                j += 1
        return ans



if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]

    print(Solution().threeSum(nums))
