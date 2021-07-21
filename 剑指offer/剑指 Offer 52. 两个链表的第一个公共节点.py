# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 16:33
# @File    : 剑指 Offer 52. 两个链表的第一个公共节点.py
from leetcode import *


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur = headA
        if not cur: return
        while cur.next:
            cur = cur.next
        cur.next = headA
        tmp = cur
        fast = slow = headB
        while True:
            if not fast or not fast.next or not fast.next.next or not slow or not slow.next:
                tmp.next = None
                return
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        slow = headB
        while slow != fast:
            slow = slow.next
            fast = fast.next
        tmp.next = None
        return fast

# 这是「差值法」的另外一种实现形式，原理同样利用「两条链表在相交节点后面的部分完全相同」。
#
# 我们令第一条链表相交节点之前的长度为 a，第二条链表相交节点之前的长度为 b，相交节点后的公共长度为 c（注意 c 可能为 00，即不存在相交节点）。
#
# 分别对两条链表进行遍历：
#
# 当第一条链表遍历完，移动到第二条链表的头部进行遍历；
# 当第二条链表遍历完，移动到第一条链表的头部进行遍历。
# 如果存在交点：第一条链表首次到达「第一个相交节点」的充要条件是第一条链表走了 a + c + ba+c+b 步，由于两条链表同时出发，并且步长相等，
# 因此当第一条链表走了 a + c + ba+c+b 步时，第二条链表同样也是走了 a + c + ba+c+b 步，即 第二条同样停在「第一个相交节点」的位置。
#
# 如果不存在交点：两者会在走完 a + c + b + ca+c+b+c 之后同时变为 nullnull，退出循环。


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A
