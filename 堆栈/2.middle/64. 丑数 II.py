# -*- coding: utf-8 -*-
# @Time    : 2021/4/11 12:26
# @File    : 64. 丑数 II.py
from leetcode import *


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res, i, j = [1], 0, 0
        while i < n:
            nums = [res[i] * 2, res[i] * 3, res[i] * 5]
            for num in nums:
                if num not in res:
                    while res[j] > num:
                        j -= 1
                    res.insert(j + 1, num)
                    j = len(res) - 1
            i += 1
        print(res)
        return res[n - 1]


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        queue, dic = [1], set()
        heapq.heapify(queue)
        while n:
            ans = heapq.heappop(queue)
            for i in [2, 3, 5]:
                tmp = ans * i
                if tmp not in dic:
                    dic.add(tmp)
                    heapq.heappush(queue, tmp)
            n -= 1
        return ans


if __name__ == '__main__':
    print(Solution().nthUglyNumber(4))
