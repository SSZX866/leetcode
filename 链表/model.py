# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 11:15
# @File    : model.py
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

# printChainToValue(buildChainWithValue([1, 5, 8, 9]))
