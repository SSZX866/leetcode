
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left==right: return head
        p, q, r, cur,i = ListNode(), ListNode(), ListNode(), head,1
        if left == 1 and right == 2 and head.next.next==None:
            p = head.next
            head.next=None
            p.next = head
            return p
        while i != right:
            if i == left-1 and left != 1:
                r = cur
            if i >= left:
                if i == left:
                    p = cur
                    q = cur.next
                    cur = q.next
                if cur:
                    q.next = p
                    p = q
                    q = cur
                    cur = cur.next
                else:
                    if left == 1:
                        q.next=p
                        head.next=None
                        return q
                    else:
                        r.next.next=None
                        q.next=p
                        r.next=q
                    return head
            else:
                cur = cur.next
            i += 1
        if left == 1:
            head.next = q
            head = p
        else:
            r.next.next = q
            r.next = p
        return head

if __name__ == '__main__':
    head = [1, 2]
    left = 1
    right = 2
    cur = ListNode(head[0])
    root = cur
    for each in head[1:]:
        p = ListNode(each)
        cur.next=p
        cur = cur.next
    cur = Solution().reverseBetween(root,left,right)
    print('[',end='')
    while cur:
        print(cur.val,end=', ')
        cur = cur.next
    print(']')

