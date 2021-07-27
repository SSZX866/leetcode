# -*- coding: utf-8 -*-
# @Time    : 2021/07/24 23:37
# @File    : 5196. 队列中可以看到的人数
from leetcode import *


# 单调栈
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        ans = []
        for height in heights[::-1]:
            if not stack:
                stack.append(height)
                ans.append(0)
            elif stack[-1] > height:
                stack.append(height)
                ans.append(1)
            else:
                cnt = 1
                while stack and stack[-1] < height:
                    stack.pop()
                    cnt += 1
                if not stack: cnt -= 1
                ans.append(cnt)
                stack.append(height)
        return ans[::-1]
