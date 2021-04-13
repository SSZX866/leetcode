# -*- coding: utf-8 -*-
# @Time    : 2021/4/1 20:21
# @File    : 654. 最大二叉树.py

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums: return None
        val = max(nums)
        index = nums.index(val)
        node = TreeNode(val)
        node.left = self.constructMaximumBinaryTree(nums[:index])
        node.right = self.constructMaximumBinaryTree(nums[index + 1:])
        return node


if __name__ == '__main__':
    nums = [3, 2, 1, 6, 0, 5]
    Solution().constructMaximumBinaryTree(nums)
