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


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next: return
        # 中间节点
        fast, mid, pre = head, head, None
        while fast and fast.next:
            pre = mid
            mid = mid.next
            fast = fast.next.next
        pre.next = None
        # 尾部反转
        cur = mid
        pre2 = None
        while cur:
            tmp = cur.next
            cur.next = pre2
            pre2 = cur
            cur = tmp
        # 合并链表
        cur1, cur2 = head, pre2
        ppr1 = None
        while cur1 and cur2:
            ppr1 = cur2
            tmp1 = cur1.next
            cur1.next = cur2
            tmp2 = cur2.next
            cur2.next = tmp1
            cur1 = tmp1
            cur2 = tmp2
        if cur2: ppr1.next = cur2


if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    printChainToValue(Solution().reorderList(buildChainWithValue(head)))
