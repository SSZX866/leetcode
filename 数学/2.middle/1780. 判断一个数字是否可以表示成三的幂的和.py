# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 14:32
# @File    : 1780. 判断一个数字是否可以表示成三的幂的和.py
from leetcode import *


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n < 1: return False
        tmp = 1
        while tmp < n:
            tmp *= 3
        if tmp == n:
            return True
        return n - tmp // 3 < tmp // 3 and self.checkPowersOfThree(n - tmp // 3)


class Solution:
    def __init__(self):
        self.help = [1]
        for i in range(15):
            self.help.append(self.help[-1] * 3)

    def checkPowersOfThree(self, n: int) -> bool:
        if n < 1: return False
        tmp = self.help[bisect.bisect(self.help, n)]
        if tmp // 3 == n:
            return True
        return n - tmp // 3 < tmp // 3 and self.checkPowersOfThree(n - tmp // 3)


# 提示 如果一个数只能被若干个 不同 的三的幂之和表示，那么它转化为三进制只能出现1和0代表该位用不用表示
# 如 12转化为三进制表示为 110 即 1*3^2+1*3^1+0*3^0 = 9+3+0
# 而 21转化为三进制表示为 210 即 2*3^2+1*3^1+0*3^0 = 2*9+3+0 使用了两个3^2 不符合题意
# 因此我们只需判断转化后的数字中是否出现除了1和0以外的数字即可
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        tmp = ''
        while n:
            tmp += str(n % 3)
            n //= 3
        print(tmp[::-1])
        return False if tmp.replace('1', '').replace('0', '') else True


if __name__ == '__main__':
    print(Solution().checkPowersOfThree(21))
