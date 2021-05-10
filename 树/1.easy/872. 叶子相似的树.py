# -*- coding: utf-8 -*-
# @Time    : 2021/5/10 15:58
# @File    : 872. 叶子相似的树.py
from leetcode import *


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        stack1, stack2, tmp = [root1], [root2], deque([])
        while stack1:
            node = stack1.pop()
            if node.right: stack1.append(node.right)
            if node.left: stack1.append(node.left)
            if not node.left and not node.right:
                tmp.append(node.val)
        while stack2:
            node = stack2.pop()
            if node.right: stack2.append(node.right)
            if node.left: stack2.append(node.left)
            if not node.left and not node.right:
                if not tmp:
                    return False
                if node.val != deque.popleft(tmp):
                    return False

        return False if tmp else True


class iterLeaf:
    def __init__(self, root):
        self.stack = [root]

    def __next__(self):
        while self.stack:
            node = self.stack.pop()
            if node.right: self.stack.append(node.right)
            if node.left: self.stack.append(node.left)
            if not node.left and not node.right:
                return node.val
        return None


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        root1, root2 = iterLeaf(root1), iterLeaf(root2)
        while True:
            tmp1, tmp2 = next(root1), next(root2)
            if None == tmp1 == tmp2:
                return True
            elif tmp1 != tmp2:
                return False


if __name__ == '__main__':
    root1 = [3, 5, 1, 6, 2, 9, 8, null, null, 7, 4]
    root2 = [3, 5, 1, 6, 7, 4, 2, null, null, null, null, null, null, 9, 8]

    # root1 = [1, 2]
    # root2 = [2, 1]

    root1, root2 = buildTreeWithValue(root1), buildTreeWithValue(root2)
    print(Solution().leafSimilar(root1, root2))
