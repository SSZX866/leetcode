# -*- coding: utf-8 -*-
# @Time    : 2021/5/15 10:25
# @File    : 1414. 和为 K 的最少斐波那契数字数目.py
from leetcode import *


class Solution:
    def __init__(self):
        self.dp = [1, 1]
        self.index = 1

    def findMinFibonacciNumbers(self, k: int) -> int:
        while self.dp[-1] < k:
            self.dp.append(self.dp[-1] + self.dp[-2])
            self.index += 1
        lo, hi = 0, self.index
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.dp[mid] < k:
                lo = mid + 1
            else:
                hi = mid
        self.index = lo
        return 1 if self.dp[lo] == k else self.findMinFibonacciNumbers(k - self.dp[lo - 1]) + 1


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        dp = [1, 1]
        while dp[-1] < k:
            dp.append(dp[-1] + dp[-2])
        # dp = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170]
        lo, hi, ans = 0, len(dp), 0
        while k:
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if dp[mid] < k:
                    lo = mid + 1
                else:
                    hi = mid
            k = k - dp[lo - 1] if dp[lo] != k else 0
            ans += 1
            lo, hi = 0, lo
        return ans


if __name__ == '__main__':
    k = 7
    k = 10
    k = 19
    print(Solution().findMinFibonacciNumbers(k))
