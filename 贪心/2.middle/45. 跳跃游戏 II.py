# -*- coding: utf-8 -*-
# @Time    : 2021/4/16 13:56
# @File    : 45. 跳跃游戏 II.py
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        i, n, ans = 0, len(nums), 0
        while i < n:
            jump = [nums[i + offset] + offset for offset in range(1, nums[i] + 1) if i + offset < n]
            if not jump or i + nums[i] >= n - 1: return ans + 1
            i += jump.index(max(jump)) + 1
            ans += 1
            print(jump, i, ans)
        return ans


# 类似BFS
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        end, start = 0, 0
        step = 0
        while start <= end:
            new_end = end
            step += 1
            for i in range(start, end + 1):
                new_end = max(nums[i] + i, new_end)
                if new_end >= len(nums) - 1:
                    return step
            start = end + 1
            end = new_end


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    nums = [1, 2, 1, 1, 1]
    print(Solution().jump(nums))
