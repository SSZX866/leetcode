# -*- coding: utf-8 -*-
# @Time    : 2021/3/26 16:15
# @File    : 61. 旋转链表.py
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 思路，直接拼接到最后，会有用例[0,1,2] 4 的情况
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next: return head
        quick, slow, cur, len = head, head, head, 0
        while cur:
            len += 1
            cur = cur.next
        while k % len:
            quick = quick.next
            k -= 1
        while quick.next:
            quick, slow = quick.next, slow.next
        quick.next = head
        head = slow.next
        slow.next = None
        return head


# # 每次旋转一次，一共旋转k次
# class Solution:
#     def rotateRight(self, head: ListNode, k: int) -> ListNode:
#         if not head or not head.next: return head
#         while k:
if __name__ == '__main__':
    head = [1]
    k = 1
    cur = ListNode(head[0])
    root = cur
    for each in head[1:]:
        p = ListNode(each)
        cur.next = p
        cur = cur.next
    cur = Solution().rotateRight(root, k)
    print('[', end='')
    while cur:
        print(cur.val, end=', ')
        cur = cur.next
    print(']')
