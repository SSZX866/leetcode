# -*- coding: utf-8 -*-
# @Time    : 2021/4/16 12:00
# @File    : 143. 重排链表.py
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def buildChainWithValue(head):
    if not head: return None
    cur = ListNode(head[0])
    root = cur
    for each in head[1:]:
        p = ListNode(each)
        cur.next = p
        cur = cur.next
    return root


def printChainToValue(root):
    print('[', end='')
    while root:
        if root.next:
            print(root.val, end=', ')
        else:
            print(root.val, end='')
        root = root.next
    print(']', end='')


class Solution:
    def reorderList(self, head: ListNode) -> ListNode:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return head
        n, cur = 0, head
        # 计算长度
        while cur:
            n += 1
            cur = cur.next
        n = n >> 1 if n % 2 else (n >> 1) - 1
        last = head
        # 找中点
        while n >= 0:
            n -= 1
            last = last.next
        pre, cur = None, last

        # #第一遍扫描，找到中点
        # fast = head
        # slow = head
        # while fast and fast.next and fast.next.next:
        #     fast = fast.next.next
        #     slow = slow.next
        # mid = slow

        # 反转中点之后的节点
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        cur, last = head, pre
        # 插入节点
        while last:
            tmp = cur.next
            cur.next = last
            last = last.next
            cur.next.next = tmp
            cur = tmp
        cur.next = None
        return head


if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    printChainToValue(Solution().reorderList(buildChainWithValue(head)))
