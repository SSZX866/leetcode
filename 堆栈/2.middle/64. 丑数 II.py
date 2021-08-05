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


# dp 用还没乘过 2 的最小丑数乘以 2；用还没乘过 3 的最小丑数乘以 3；用还没乘过 5 的最小丑数乘以 5。然后在得到的数字中取最小，就是新的丑数。
#  index2, index3, index5 分别表示丑数集合中还没乘过 2，3，5 的丑数位置
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        index1, index2, index3 = 0, 0, 0
        dp[0] = 1
        for i in range(1, n):
            dp[i] = min(dp[index1] * 2, dp[index2] * 3, dp[index3] * 5)
            if dp[i] == dp[index1] * 2: index1 += 1
            if dp[i] == dp[index2] * 3: index2 += 1
            if dp[i] == dp[index3] * 5: index3 += 1
        return dp[-1]


if __name__ == '__main__':
    print(Solution().nthUglyNumber(4))
