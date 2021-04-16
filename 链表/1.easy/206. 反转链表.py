# -*- coding: utf-8 -*-
# @Time    : 2021/4/15 19:33
# @File    : 206. 反转链表.py
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
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            last = cur.next
            cur.next = pre
            pre = cur
            cur = last
        return pre


if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    printChainToValue(Solution().reverseList(buildChainWithValue(head)))
