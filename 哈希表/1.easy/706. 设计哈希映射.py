class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = {}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.hash[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.hash:
            return self.hash[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.hash:
            del self.hash[key]


# 链地址法
class Node:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.base = 769
        self.dic = [Node() for _ in range(self.base)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        head = self.dic[key % self.base]
        cur = head.next
        while cur:
            if cur.key == key:
                cur.val = value
                return
            cur = cur.next
        cur = Node(key, value)
        cur.next = head.next
        head.next = cur

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        head = self.dic[key % self.base]
        head = head.next
        while head:
            if head.key == key:
                return head.val
            head = head.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        head = self.dic[key % self.base]
        if self.get(key) == -1: return
        while head.next.key != key:
            head = head.next
        head.next = head.next.next
