# -*- coding: utf-8 -*-
# @Time    : 2021/4/1 18:31
# @File    : 1551. 使数组中所有元素相等的最小操作数.py
class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2: return (n // 2 + 1) * (n // 2)
        return sum(i * 2 + 1 for i in range(int(n / 2)))
        # return (n // 2 + 1) * (n // 2) if n % 2 else sum(i * 2 + 1 for i in range(int(n / 2)))


if __name__ == '__main__':
    print(Solution().minOperations(3))
