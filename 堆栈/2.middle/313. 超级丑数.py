# -*- coding: utf-8 -*-
# @Time    : 2021/4/20 16:34
# @File    : 313. 超级丑数.py
from leetcode import *


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap, dic = [1], set()
        while n > 1:
            ans = heapq.heappop(heap)
            for prime in primes:
                tmp = ans * prime
                if tmp not in dic:
                    dic.add(tmp)
                    heapq.heappush(heap, tmp)
            n -= 1
        return heapq.heappop(heap)


if __name__ == '__main__':
    n = 1
    primes = [2, 7, 13, 19]
    print(Solution().nthSuperUglyNumber(n, primes))
