# -*- coding: utf-8 -*-
# @Time    : 2021/4/14 19:27
# @File    : 146. LRU 缓存机制.py
class LRUCache:

    def __init__(self, capacity: int):
        self.dic = {}
        self.queue = []
        self.MAXLENGTH = capacity

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        index = self.queue.index(key)
        self.queue = self.queue[:index] + self.queue[index + 1:] + [key]
        return self.dic[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.dic:
            if len(self.queue) == self.MAXLENGTH:
                self.dic.pop(self.queue.pop(0))
            self.queue.append(key)
        else:
            index = self.queue.index(key)
            self.queue = self.queue[:index] + self.queue[index + 1:] + [key]
        self.dic[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
if __name__ == '__main__':
    obj = LRUCache(2)
    obj.put(2, 1)
    obj.put(1, 1)
    obj.put(2, 3)
    obj.put(4, 1)
    print(obj.get(1))
    print(obj.get(2))
