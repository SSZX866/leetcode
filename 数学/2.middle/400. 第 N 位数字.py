# -*- coding: utf-8 -*-
# @Time    : 2021/11/30 09:27
# @File    : 400. 第 N 位数字.py
from leetcode import *


# 1位数 9个 ===> 1 * 9
# 2位数 90个 ===> 2 * 90
# 3位数 900个 ===> 3 * 900
# ...
# https://leetcode-cn.com/problems/nth-digit/solution/pythonjavajavascriptgo-jian-dan-mo-ni-by-kk3x/

class Solution:
    def findNthDigit(self, n: int) -> int:
        # n = 200
        cur, base = 9, 0
        # 判断几位数
        while n > cur:
            base += 1
            cur += 10 ** base * 9 * (base + 1)
        base += 1
        # base = 3
        # 判断该数是base位数中的第x位
        # x = 200 - 189 = 11
        x = n - (cur - 10 ** (base - 1) * 9 * base)
        # 转换至下标从0开始
        # x = 11 - 1 = 10
        x -= 1
        # 计算该数为10进制中的第x位
        # b = 10 // 3 = 3
        b = x // base
        # 计算x位中第x个数是多少
        # num = 10 ** 2 + 3 = 103
        num = 10 ** (base - 1) + b
        # 判断需要取第几位
        # bit = 10 % 3 = 1
        bit = x % base
        # 从左往右第bit位 = 从右往左第base - bit - 1位
        for i in range(base - bit - 1):
            num //= 10
        return num % 10


if __name__ == '__main__':
    print(Solution().findNthDigit(101))
