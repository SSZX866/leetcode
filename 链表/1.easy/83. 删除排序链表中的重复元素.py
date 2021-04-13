# -*- coding: utf-8 -*-
# @Time    : 2021/3/26 14:39
# @File    : 83. 删除排序链表中的重复元素.py
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        tail = dummy = ListNode(val=None, next=head)
        while head:
            if head.val != tail.val:
                tail.next = head
                tail = tail.next
            head = head.next
        tail.next = None
        return dummy.next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head
        head, nums = head, []
        while head:
            nums.append(head.val)
            head = head.next
        nums = sorted(list(set(nums)))
        cur = ListNode(nums[0])
        root = cur
        for each in nums[1:]:
            p = ListNode(each)
            cur.next = p
            cur = cur.next
        return root


if __name__ == '__main__':
    head = [1,1,1,1,2,2,2]
    cur = ListNode(head[0])
    root = cur
    for each in head[1:]:
        p = ListNode(each)
        cur.next = p
        cur = cur.next
    cur = Solution().deleteDuplicates(root)
    print('[', end='')
    while cur:
        print(cur.val, end=', ')
        cur = cur.next
    print(']')
