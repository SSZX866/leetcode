# -*- coding: utf-8 -*-
# @Time    : 2021/07/29 11:40
# @File    : 1104. 二叉树寻路
from leetcode import *


class Solution:
    # 类变量保存每层最小和最大数字
    start = [2 ** i for i in range(32)]
    end = [2 ** (i + 1) - 1 for i in range(32)]

    def pathInZigZagTree(self, label: int) -> List[int]:
        # 计算 label 所在层
        level = -1
        for i in range(32):
            if self.start[i] > label:
                level = i - 1
                break

        ans = [label]
        cur = label
        # 自底向上, 每层都利用对称性翻转一次
        for i in range(level - 1, -1, -1):
            cur = self.start[i] + self.end[i] - cur // 2
            ans.append(cur)

        ans.reverse()
        return ans
