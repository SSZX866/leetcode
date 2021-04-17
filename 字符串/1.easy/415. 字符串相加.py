# -*- coding: utf-8 -*-
# @Time    : 2021/4/16 17:51
# @File    : 415. 字符串相加.py
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2): num1, num2 = num2, num1
        m, n = len(num1), len(num2)  # m<=n
        num1 = '0' * (n - m) + num1
        i, add, ans = n - 1, 0, ""
        while i >= 0:
            a, b = int(num1[i]), int(num2[i])
            ans = str((a + b + add) % 10) + ans
            add = (a + b + add) // 10
            i -= 1
        if add: ans = '1' + ans
        return ans


if __name__ == '__main__':
    print(Solution().addStrings('1', '199'))
