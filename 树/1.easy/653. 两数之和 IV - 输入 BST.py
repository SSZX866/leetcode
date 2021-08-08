# -*- coding: utf-8 -*-
# @Time    : 2021/08/08 18:02
# @File    : 653. 两数之和 IV - 输入 BST
from leetcode import *


# 本题可用对撞指针

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        dic = set()

        def f(root, k):
            if not root: return False
            if root.val in dic: return True
            dic.add(k - root.val)
            return True if f(root.left, k) or f(root.right, k) else False

        return f(root, k)


# 递归代码在运行多个用例时会出现bug，比如将所有测试用例全部输入时，从第二个用例开始结果不正确，而单独运行某个用例又是正确的，
# 猜想时力扣运行代码的时候只是循环调用findTarget函数，并没有清空所有变量。
class Solution:
    dic = set()

    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root: return False
        if root.val in self.dic: return True
        self.dic.add(k - root.val)
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)
