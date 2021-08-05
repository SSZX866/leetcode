# -*- coding: utf-8 -*-
# @Time    : 2021/4/19 16:20
# @File    : 47. 全排列 II.py
from leetcode import *


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        print(id(nums))  # 140208276450192

        def dfs(x):
            if x == len(nums) - 1:
                print(nums, nums[:])  # 打印的都是[1, 2, 1]
                print(id(nums[:]), id(nums))  # 140208276372688 140208276450192
                # res.append(nums) # 添加的是[1, 1, 2]
                res.append(nums[:])  # 添加的是[1, 2, 1]
                return
            dic = set()
            for i in range(x, len(nums)):
                if nums[i] in dic: continue
                dic.add(nums[i])
                nums[i], nums[x] = nums[x], nums[i]
                dfs(x + 1)
                nums[i], nums[x] = nums[x], nums[i]

        res = []
        dfs(0)
        return res


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for c in nums:
            ans = [num[:i] + [c] + num[i:] for num in ans for i in range((num + [c]).index(c) + 1)]
        return ans


# 过程中去重
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(path, ns):
            if not ns and path[:] not in ans:
                ans.append(path[:])
            for i in range(len(ns)):
                path.append(ns[i])
                backtrack(path, ns[:i] + ns[i + 1:])
                path.pop()

        backtrack([], nums)
        return ans


# 最后再去重
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(path, ns):
            if not ns:
                ans.append(tuple(path[:]))
            for i in range(len(ns)):
                path.append(ns[i])
                backtrack(path, ns[:i] + ns[i + 1:])
                path.pop()

        backtrack([], nums)
        return list(map(list, set(ans)))


if __name__ == '__main__':
    nums = [1, 1, 2]
    s = 'a'
    s.isdigit()
    print(Solution().permuteUnique(nums))
