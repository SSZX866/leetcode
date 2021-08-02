# -*- coding: utf-8 -*-
# @Time    : 2021/3/25 09:54
# @File    : 82. 删除排序链表中的重复元素 II.py
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head
        nums = []
        num = None
        while head:
            if not nums or nums[-1] == head.val:
                nums.append(head.val)
            else:
                while len(nums) >= 2 and nums[-1] == nums[-2]:
                    num = nums.pop()
                if nums and nums[-1] == num:
                    nums.pop()
                nums.append(head.val)
            head = head.next
            while len(nums) >= 2 and nums[-1] == nums[-2]:
                num = nums.pop()
            if nums and nums[-1] == num:
                nums.pop()
        print(nums)
        if not nums: return None
        cur = ListNode(nums[0])
        root = cur
        for each in nums[1:]:
            p = ListNode(each)
            cur.next = p
            cur = cur.next
        return root


# 我们会确保「进入外层循环时 head 不会与上一节点相同」，因此插入时机：
#
# head 已经没有下一个节点，head 可以被插入
#
# head 有一下个节点，但是值与 head 不相同，head 可以被插入

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        tail = dummy = ListNode(val=None, next=head)
        while head:
            if not head.next or head.next.val != head.val:
                tail.next = head
                tail = tail.next
            while head.next and head.val == head.next.val:
                head = head.next
            head = head.next
        tail.next = None
        return dummy.next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur:
            tmp = cur
            while cur.next and cur.next.val == cur.val:
                cur = cur.next
            cur = cur.next
            tmp.next = cur
        return head


if __name__ == '__main__':
    head = [1, 1, 1]
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
