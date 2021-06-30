# -*- coding: utf-8 -*-
# @Time    : 2021/6/30 15:42
# @File    : 剑指 Offer 37. 序列化二叉树.py
from leetcode import *


class Codec:

    def serialize(self, root):
        if not root: return None
        queue = deque([root])
        ans = []
        cnt = 1  # 记录节点的个数
        while queue:
            tmp = queue.popleft()
            if cnt:
                if tmp:
                    ans.append(tmp.val)
                    cnt -= 1
                else:
                    ans.append(None)
            if tmp:
                queue.append(tmp.left)
                queue.append(tmp.right)
                if tmp.left:
                    cnt += 1
                if tmp.right:
                    cnt += 1
        return str(ans).replace('None', 'null')

    # def deserialize(self, data):
    #     if not data: return None
    #     root = json.loads(data)
    #     tree = TreeNode(root[0])
    #     queue = [tree]
    #     i = 1
    #     while i < len(root):
    #         node = queue.pop(0)
    #         if root[i] is None:
    #             i += 1
    #             if i < len(root) and root[i] != None:
    #                 node.right = TreeNode(root[i])
    #                 queue.append(node.right)
    #             i += 1
    #         else:
    #             node.left = TreeNode(root[i])
    #             queue.append(node.left)
    #             i += 1
    #             if i < len(root) and root[i] != None:
    #                 node.right = TreeNode(root[i])
    #                 queue.append(node.right)
    #             i += 1
    #     return tree

    def deserialize(self, data):
        if not data: return None
        data = json.loads(data)
        root = TreeNode(data[0])
        que = deque()
        isLeft = True
        parent = root
        for each in data[1:]:
            if each is not None:
                tmp = TreeNode(each)
            else:
                tmp = None
            if isLeft:
                parent.left = tmp
            else:
                parent.right = tmp
            if tmp is not None:
                que.append(tmp)
            isLeft = not isLeft
            if isLeft:
                parent = que.popleft()
        return root


if __name__ == '__main__':
    t = buildTreeWithValue([1, 2, 3, 4, None, 5])
    t = buildTreeWithValue([])
    print(Codec().serialize(t))
