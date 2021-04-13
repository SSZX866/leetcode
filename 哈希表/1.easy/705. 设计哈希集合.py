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