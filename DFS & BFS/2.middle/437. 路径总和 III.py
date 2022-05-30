# -*- coding: utf-8 -*-
# @Time    : 2021/9/28 10:30
# @File    : 437. 路径总和 III.py
from leetcode import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# [1,-2,-3,1,3,-2,null,-1] -2 案例未通过
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root: return 0
        ans = 0 if root.val != targetSum else 1

        def dfs(pre, dic, node):
            nonlocal ans
            if not node: return
            ans += dic[node.val]
            dic = collections.defaultdict(int)
            for i in range(len(pre)):
                pre[i] += node.val
                dic[targetSum - pre[i]] += 1
            pre.append(node.val)
            dic[targetSum - node.val] += 1
            if node.left: dfs(pre, dic, node.left)
            if node.right: dfs(pre, dic, node.right)
            if node != root and (not node.left or not node.right):
                if node.val == targetSum:
                    ans += 1
            pre.pop()
            dic[targetSum - node.val] -= 1
            for i in range(len(pre)):
                dic[targetSum - pre[i]] -= 1
                pre[i] -= node.val

        # node = TreeNode(val=-1001, left=root)
        dic = collections.defaultdict(int)
        dfs([], dic, root)
        return ans


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root: return 0

        def dfs(dic, curSum, node):
            if not node: return 0
            # curSum - pre = targetSum
            curSum += node.val
            ans = dic[curSum - targetSum]
            dic[curSum] += 1
            ans += dfs(dic, curSum, node.left)
            ans += dfs(dic, curSum, node.right)
            dic[curSum] -= 1
            return ans

        d = collections.defaultdict(int)
        d[0] = 1
        return dfs(d, 0, root)
