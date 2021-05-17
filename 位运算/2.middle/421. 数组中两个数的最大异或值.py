# -*- coding: utf-8 -*-
# @Time    : 2021/5/16 13:19
# @File    : 421. 数组中两个数的最大异或值.py
from leetcode import *


class Tree:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        n, root, ans = len(bin(max(nums))[2:]), Tree(), 0
        for num in nums:
            b = bin(num)[2:]
            b = '0' * (n - len(b)) + b
            cur = root
            for each in b:
                if each == '1':
                    if not cur.left:
                        cur.left = Tree(1)
                    cur = cur.left
                else:
                    if not cur.right:
                        cur.right = Tree(0)
                    cur = cur.right
        for num in nums:
            b = bin(num)[2:]
            b = '0' * (n - len(b)) + b
            tmp, cur = '', root
            for each in b:
                if each == '0':
                    if cur.left:
                        cur = cur.left
                        tmp += '1'
                    else:
                        cur = cur.right
                        tmp += '0'
                else:
                    if cur.right:
                        cur = cur.right
                        tmp += '1'
                    else:
                        cur = cur.left
                        tmp += '0'
            ans = max(ans, int(tmp, 2))
        return ans


if __name__ == '__main__':
    nums = [8, 10, 2]
    nums = [3, 10, 5, 25, 2, 8]
    print(Solution().findMaximumXOR(nums))
