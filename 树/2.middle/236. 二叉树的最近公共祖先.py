# -*- coding: utf-8 -*-
# @Time    : 2021/4/14 19:58
# @File    : 236. 二叉树的最近公共祖先.py

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTreeWithValue(root):
    if not root: return root
    tree = TreeNode(root[0])
    queue = [tree]
    i = 1
    while i < len(root):
        node = queue.pop(0)
        if root[i] == None:
            i += 1
            if i < len(root) and root[i] != None:
                node.right = TreeNode(root[i])
                queue.append(node.right)
            i += 1
        else:
            node.left = TreeNode(root[i])
            queue.append(node.left)
            i += 1
            if i < len(root) and root[i] != None:
                node.right = TreeNode(root[i])
                queue.append(node.right)
            i += 1
    return tree


# 1.当 left 和 right 同时为空：说明 root 的左/右子树中都不包含 p,q，返回null；
# 2.当left 和right 同时不为空 ：说明 p,q 分列在root 的 异侧 （分别在 左 / 右子树），因此root为最近公共祖先，返回root；
# 3.left 为空 ，right 不为空：p,q 都不在 root 的左子树中，直接返回 right 。
# 具体可分为两种情况：
#     1.p,q 其中一个在root的 右子树中，此时 right 指向p（假设为 p)
#     2.p,q 两节点都在 root 的 右子树 中，此时的right 指向 最近公共祖先节点 ；
# 4.当 left 不为空 ， right 为空 ：与情况 3. 同理

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right: return   # 1.
        if not left: return right  # 3.
        if not right: return left  # 4.
        return root  # 2. if left and right:

