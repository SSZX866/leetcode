# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 11:10
# @File    : 5802. 统计好数字的数目.py
from leetcode import *


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def superPow(a: int, b: List[int],base) -> int:
            if not b:
                return 1
            b = list(map(int,b))
            last = b.pop()

            part1 = (a ** last) % base
            part2 = (superPow(a, b,base) ** 10) % base

            return (part1 * part2) % base

        def quickPow(a, b, c):
            ans = 1
            while b > 0:
                if b % 2 == 1:
                    ans = ans * a % c
                a = a * a % c
                b = b / 2
            return ans % c


        # 2 3 5 7
        tmp = math.ceil(n / 2)
        # return (quickPow(5, tmp, 1000000007) * quickPow(4, (n - tmp), 1000000007)) % 1000000007
        return (superPow(5, list(str(tmp)), 1000000007) * superPow(4, list(str(n - tmp)), 1000000007)) % 1000000007


if __name__ == '__main__':
    for i in range(10):
        print(Solution().countGoodNumbers(i))
