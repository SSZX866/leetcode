# -*- coding: utf-8 -*-
# @Time    : 2021/6/1 16:52
# @File    : 1769. 移动所有球到每个盒子所需的最小操作数.py
from leetcode import *


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        for i in range(len(boxes)):
            ans.append(0)
            for j in range(len(boxes)):
                if boxes[j] == '1': ans[-1] += abs(j - i)
        return ans


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans, pre = [], [0]
        for box in boxes:
            pre.append(pre[-1] + 1) if box == '1' else pre.append(pre[-1])
        dp = [sum(i * int(boxes[i]) for i in range(1, len(boxes)))]
        for i in range(1, len(boxes)):
            left = pre[i]
            right = pre[-1] - left
            dp.append(dp[-1] + left - right)
        return dp


if __name__ == '__main__':
    boxes = "001011"
    # 输出：[11, 8, 5, 4, 3, 4]
    print(Solution().minOperations(boxes))
