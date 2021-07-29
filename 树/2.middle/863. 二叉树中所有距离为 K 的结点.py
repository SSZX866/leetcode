# -*- coding: utf-8 -*-
# @Time    : 2021/07/28 10:51
# @File    : 863. 二叉树中所有距离为 K 的结点
from leetcode import *


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k: return [target.val]
        if not root: return []
        root.parent = None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                node.left.parent = node
            if node.right:
                queue.append(node.right)
                node.right.parent = node

        def generateNode(node):
            if not node: return []
            res = []
            if node.left: res.append(node.left)
            if node.right: res.append(node.right)
            if node.parent: res.append(node.parent)
            return res

        if not target: return []
        queue = deque([target])
        ans = []
        visit = {target.val}
        while queue:
            cur_que = queue
            queue = deque()
            k -= 1
            while cur_que:
                node = cur_que.pop()
                for next_node in generateNode(node):
                    if next_node.val in visit:
                        continue
                    visit.add(next_node.val)
                    queue.append(next_node)
                    if not k: ans.append(next_node.val)
            if not k: return ans
        return ans
