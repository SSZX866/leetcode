# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 10:07
# @File    : 263. 丑数.py
class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1: return False
        while not n % 5:
            n //= 5
        while not n % 3:
            n //= 3
        while not n % 2:
            n >>= 1
        return True if n == 1 else False


if __name__ == '__main__':
    print(Solution().isUgly(6))
