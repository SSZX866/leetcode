# -*- coding: utf-8 -*-
# @Time    : 2021/07/28 20:33
# @File    : 84. 柱状图中最大的矩形
from leetcode import *


# 单调栈 栈内应存下标
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        ans = 0
        for i in range(len(heights)):
            if not stack or heights[stack[-1]] < heights[i]:
                stack.append(i)
            else:
                while heights[stack[-1]] > heights[i]:
                    H = heights[stack.pop()]
                    W = i - stack[-1] - 1
                    ans = max(ans, H * W)
                stack.append(i)
        return ans


if __name__ == '__main__':
    # heights = [2, 1, 2]
    heights = [4, 2, 0, 3, 2, 5]
    print(Solution().largestRectangleArea(heights))
