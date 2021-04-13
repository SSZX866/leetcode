# -*- coding: utf-8 -*-
# @Time    : 2021/3/31 15:53
# @File    : 78. 子集.py
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            n = len(ans)
            while n:
                n -= 1
                ans += [ans[n] + [num]]
        return ans


# 回溯 https://www.bilibili.com/video/BV1HD4y1Q7Te?from=search&seid=12055137674583817336
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []

        def backtrack(index, nums, res, path):
            res.append(path[:])
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, nums, res, path)
                path.pop()

        backtrack(0, nums, res, path)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().subsets(nums))
