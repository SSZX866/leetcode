# -*- coding: utf-8 -*-
# @Time    : 2021/3/24 14:56
# @File    : 456. 132模式.py
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [nums[-1]]
        stack_temp = []
        k = stack[0]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < stack[-1]:
                while stack and nums[i] < stack[-1]:
                    stack_temp.append(stack.pop())
                stack.append(nums[i])
                print(stack[-1])
                while stack_temp:
                    stack.append(stack_temp.pop())
            else:
                stack.append(nums[i])
            print(stack)
        return False


# time o(n^2)
# class Solution:
#     def find132pattern(self, nums: List[int]) -> bool:
#         if len(set(nums)) < 3: return False
#         n = len(nums)
#         for i in range(1, n - 1):
#             for j in range(i+1, n):
#                 num1, num3 = min(nums[:i]), max(nums[i:j])
#                 for k in range(j, n):
#                     if num1 < nums[k] < num3:
#                         return True
#         return False

if __name__ == '__main__':
    nums = [1,2,3,4]
    print(Solution().find132pattern(nums))
