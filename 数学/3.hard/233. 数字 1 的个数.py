# -*- coding: utf-8 -*-
# @Time    : 2021/08/13 09:57
# @File    : 233. 数字 1 的个数
from leetcode import *
class Solution:
    def countDigitOne(self, n: int) -> int:
        # 0-9: 1
        # 0-99: 10 + 10 * 1 = 20
        # 0-999: 100 + 10 * 20 = 300
        # 0-9999: 1000 + 10 * 300 = 4000
        # 0-99999: 10000 + 10 * 4000 = 50000
        # ...
        ans, i, num = 0, 1, n
        while n:
            if n % 10 == 0: ans += (n // 10) * i
            if n % 10 == 1: ans += (n // 10) * i + (num % i) + 1
            if n % 10 > 1: ans += math.ceil(n / 10) * i
            n //= 10
            i *= 10
        return ans