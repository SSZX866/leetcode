# -*- coding: utf-8 -*-
# @Time    : 2021/4/16 15:09
# @File    : 剑指 Offer 22. 链表中倒数第k个节点.py
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
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        slow = fast = head
        while fast:
            if k <= 0:
                slow = slow.next
            fast = fast.next
            k -= 1
        return slow


if __name__ == '__main__':
    head = [1, 2, 3, 4, 5]
    k = 2
    printChainToValue(Solution().getKthFromEnd(buildChainWithValue(head), k))
