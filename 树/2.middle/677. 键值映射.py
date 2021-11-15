# -*- coding: utf-8 -*-
# @Time    : 2021/11/15 09:27
# @File    : 677. 键值映射.py
from leetcode import *


class Trie:
    def __init__(self):
        self.val = -1
        self.next = dict()


class MapSum:

    def __init__(self):
        self.root = Trie()

    def insert(self, key: str, val: int) -> None:
        node = self.root
        i, n = 0, len(key)
        while i < n:
            if key[i] not in node.next:
                node.next[key[i]] = Trie()
            node = node.next[key[i]]
            i += 1
        node.val = val

    def sum(self, prefix: str) -> int:
        node = self.root
        res = 0
        i, n = 0, len(prefix)
        while i < n and prefix[i] in node.next:
            node = node.next[prefix[i]]
            i += 1
        if i != n: return res
        if node.val != -1: res += node.val
        queue = collections.deque([node.next])
        while queue:
            nextNode = queue.popleft()
            for key in nextNode:
                if nextNode[key].val != -1: res += nextNode[key].val
                queue.append(nextNode[key].next)
        return res

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
