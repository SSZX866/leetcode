# -*- coding: utf-8 -*-
# @Time    : 2021/07/31 18:04
# @File    : 987. 二叉树的垂序遍历
from leetcode import *


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = deque([(root, 0, 0)])
        dic = defaultdict(list)
        while queue:
            node, row, col = queue.pop()
            if node.left: queue.append((node.left, row + 1, col - 1))
            if node.right: queue.append((node.right, row + 1, col + 1))
            dic[col].append((row, node.val))

        # ans = []
        # for key in sorted(dic.keys()):
        #     ans.append([each[1] for each in sorted(dic[key], key=lambda x: (x[0], x[1]))])
        # return ans
        return [[each[1] for each in sorted(dic[key], key=lambda x: (x[0], x[1]))] for key in sorted(dic.keys())]
