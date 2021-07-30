# -*- coding: utf-8 -*-
# @Time    : 2021/3/26 15:50
# @File    : 19. 删除链表的倒数第 N 个结点.py
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head: return head
        nodes, cur = [], head
        while cur:
            nodes.append(cur)
            cur = cur.next
        if n == len(nodes):
            return head.next
        elif n == 1:
            nodes[-2].next = None
        elif n == 0:
            pass
        else:
            nodes[0 - n - 1].next = nodes[0 - n + 1]
        return head


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        slow, fast, pre = head, head, dummy
        while fast:
            if n:
                fast = fast.next
                n -= 1
            else:
                pre = slow
                fast = fast.next
                slow = slow.next
        pre.next = slow.next
        return dummy.next


if __name__ == '__main__':
    head = [1, 2, 3, 4]
    n = 0
    cur = ListNode(head[0])
    root = cur
    for each in head[1:]:
        p = ListNode(each)
        cur.next = p
        cur = cur.next
    cur = Solution().removeNthFromEnd(root, n)
    print('[', end='')
    while cur:
        print(cur.val, end=', ')
        cur = cur.next
    print(']')
