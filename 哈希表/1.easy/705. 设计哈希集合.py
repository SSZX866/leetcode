class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = []

    def add(self, key: int) -> None:
        self.hash.append(key)

    def remove(self, key: int) -> None:
        for i in range(len(self.hash)):
            if self.hash[i] == key:
                self.hash[i] = None

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        for i in range(len(self.hash)):
            if self.hash[i] == key:
                return True
        return False


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = {}

    def add(self, key: int) -> None:
        if key in self.hash:
            self.hash[key] += 1
        else:
            self.hash[key] = 1

    def remove(self, key: int) -> None:
        if key in self.hash:
            del self.hash[key]

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.hash


# 2021-9-7
# 链地址法解决冲突
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.base = 769
        self.dic = [Node() for _ in range(self.base)]

    def add(self, key: int) -> None:
        if self.contains(key): return
        head = self.dic[key % self.base]
        cur = Node(key)
        cur.next = head.next
        head.next = cur

    def remove(self, key: int) -> None:
        if not self.contains(key): return
        head = self.dic[key % self.base]
        while head.next.val != key:
            head = head.next
        head.next = head.next.next

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        head = self.dic[key % self.base]
        head = head.next
        while head:
            if head.val == key:
                return True
            head = head.next
        return False
