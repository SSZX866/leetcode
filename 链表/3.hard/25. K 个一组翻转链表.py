# -*- coding: utf-8 -*-
# @Time    : 2021/4/16 15:42
# @File    : 25. K 个一组翻转链表.py
from leetcode import *


# 栈
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        stack = []
        p = ListNode(0)
        result = p

        flag = True
        while head:
            for i in range(k):
                if not head:
                    return result.next
                stack.append(head)
                head = head.next
            while stack:
                cur = stack.pop()
                p.next = cur
                p = cur
            p.next = head
        return result.next


# 链表操作
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k < 2: return head
        dummy = ListNode()
        dummy.next = head
        pre, p, q, cnt = dummy, head, head, 1
        while q and q.next:
            q = q.next
            cnt += 1
            if k == cnt:
                last = q.next
                pre.next, tmp = self.reveseSector(p, q)
                tmp.next = last
                pre = tmp
                cnt = 1
                p = q = last
        return dummy.next

    def reveseSector(self, head, tail):
        # 反转[head,tail]之间的字符串
        p, q, l = head, head.next, head.next.next
        while q != tail:
            q.next = p
            p = q
            q = l
            l = l.next
        q.next = p
        return q, head


if __name__ == '__main__':
    head, k = [1, 2, 3, 4, 5], 2
    head, k = [1, 2], 2
    head = buildChainWithValue(head)
    printChainToValue(Solution().reverseKGroup(head, k))
    # a, b = Solution().reveseSector(head, head.next.next)
    # while b != a:
    #     print(a.val)
    #     a = a.next
    # print(a.val)
