# -*- coding: utf-8 -*-
# @Time    : 2021/08/05 13:06
# @File    : 101. 对称二叉树
from leetcode import *


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.check(root.left, root.right)

    def check(self, left, right):
        if not left or not right:
            return not left and not right
        return left.val == right.val and self.check(left.left, right.right) and self.check(right.left, left.right)


# 模拟递归用栈实现
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        a, b = [root], [root]
        while a and b:
            left, right = a.pop(), b.pop()
            if left.val != right.val: return False
            if left.left and right.right:
                a.append(left.left)
                b.append(right.right)
            if left.right and right.left:
                a.append(left.right)
                b.append(right.left)
            if (left.left and not right.right) or (left.right and not right.left):
                return False
            if (not left.left and right.right) or (not left.right and right.left):
                return False
        return True


# 层次遍历检测是否为回文
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = deque([root])
        while queue:
            cur = queue
            queue = deque()
            tmp = []
            while cur:
                node = cur.popleft()
                if node:
                    tmp.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    tmp.append(None)
            for i in range(len(tmp) // 2):
                if tmp[i] != tmp[- i - 1]:
                    return False
        return True
