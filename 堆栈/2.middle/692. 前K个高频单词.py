# -*- coding: utf-8 -*-
# @Time    : 2021/5/20 15:44
# @File    : 692. 前K个高频单词.py
from leetcode import *


class Word:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __lt__(self, other):
        if self.a != other.a:
            return self.a < other.a
        return self.b > other.b


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = []
        for key in count:
            if len(heap) < k:
                heapq.heappush(heap, Word(count[key], key))

            elif heap[0].a < count[key] or (heap[0].a == count[key] and heap[0].b > key):
                heapq.heappop(heap)
                heapq.heappush(heap, Word(count[key], key))
        ans = [each.b for each in heapq.nsmallest(k, heap)]
        return ans[::-1]


if __name__ == '__main__':
    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 4
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 3
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 1
    words = ["aaa", "aa", "a"]
    k = 2
    print(Solution().topKFrequent(words, k))
