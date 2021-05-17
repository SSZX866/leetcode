# -*- coding: utf-8 -*-
# @Time    : 2021/5/17 21:47
# @File    : 993. 二叉树的堂兄弟节点.py
from leetcode import *


# 层次遍历+补充满二叉树
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if x == root.val or y == root.val: return False
        queue, cur, layer = deque([root]), deque([]), []
        while queue:
            layer.append([])
            flag = False
            while queue:
                node = queue.popleft()
                layer[-1].append(node.val)
                if node.left:
                    cur.append(node.left)
                    flag = True
                else:
                    cur.append(TreeNode(0))
                if node.right:
                    cur.append(node.right)
                    flag = True
                else:
                    cur.append(TreeNode(0))
            if not flag: break
            queue = cur
            cur = deque([])
        for i in range(len(layer)):
            if x in layer[i] and y in layer[i]:
                if layer[i].index(x) // 2 == layer[i].index(y) // 2:
                    return False
                else:
                    return True
            elif x not in layer[i] and y not in layer[i]:
                continue
            else:
                return False


# 层次遍历+字典
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if x == root.val or y == root.val: return False
        queue, cur, dic, layer = deque([root]), deque([]), {}, []
        while queue:
            layer.append([])
            while queue:
                node = queue.popleft()
                layer[-1].append(node.val)
                if node.left:
                    dic[node.left.val] = node.val
                    cur.append(node.left)
                if node.right:
                    dic[node.right.val] = node.val
                    cur.append(node.right)
            queue = cur
            cur = deque([])
        print(dic, layer)
        if dic[x] == dic[y]: return False
        for eachLayer in layer:
            if (x in eachLayer and y not in eachLayer) or (y in eachLayer and x not in eachLayer):
                return False
            elif x in eachLayer and y in eachLayer:
                return True
        return False
