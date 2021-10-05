# -*- coding: utf-8 -*-
# @Time    : 2021/10/5 19:33
# @File    : 284. 窥探迭代器.py
from leetcode import *


# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.queue = []

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.queue:
            self.queue.append(self.iterator.next())
        return self.queue[0]

    def next(self):
        """
        :rtype: int
        """
        if self.queue:
            return self.queue.pop()
        return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.queue:
            return True
        return self.iterator.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
