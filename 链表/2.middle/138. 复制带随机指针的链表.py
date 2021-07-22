# -*- coding: utf-8 -*-
# @Time    : 2021/07/22 13:34
# @File    : 138. 复制带随机指针的链表
from leetcode import *


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        random_dict = dict()
        chain_table = dict()
        #  存储链表结构
        tmp = head
        i = 0
        while tmp:
            chain_table[tmp] = i
            tmp = tmp.next
            i += 1
        # 存储原链表的random结构
        i = 0
        tmp = head
        while tmp:
            if tmp.random is not None:
                random_dict[i] = chain_table[tmp.random]
            else:
                random_dict[i] = None
            tmp = tmp.next
            i += 1

        # 构建新链表
        dummy = Node(0)
        tmp = head
        tmp1 = dummy
        new_chain_table = dict()
        i = 0
        while tmp:
            tmp1.next = Node(tmp.val)
            new_chain_table[i] = tmp1.next
            tmp1 = tmp1.next
            tmp = tmp.next
            i += 1
        # 构建random指针
        tmp = dummy
        i = 0
        while tmp.next:
            if random_dict[i] is not None:
                tmp.next.random = new_chain_table[random_dict[i]]
            else:
                tmp.next.random = None
            tmp = tmp.next
            i += 1

        return dummy.next


# 原地算法
# 将每个复制插在原来的结点后面
# 这样做的意义是我们可以通过原random指针的位置，判断新的random指针要指向该random指针的next即可。
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return head
        cur = head
        # 创建节点在原节点后面
        while cur:
            tmp = cur.next
            cur.next = Node(cur.val)
            cur.next.next = tmp
            cur = tmp
        cur = head
        # 更新random指针
        while cur:
            if cur.random is not None:
                cur.next.random = cur.random.next
            cur = cur.next.next
        cur = head.next
        # 删除旧节点
        while cur.next:
            cur.next = cur.next.next
            cur = cur.next
        return head.next
