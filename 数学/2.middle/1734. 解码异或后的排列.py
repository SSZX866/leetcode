# -*- coding: utf-8 -*-
# @Time    : 2021/5/11 10:41
# @File    : 1734. 解码异或后的排列.py
from leetcode import *


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n, first = len(encoded), 0
        for i in range(1, n + 2):
            first ^= i
        for each in encoded[1::2]:
            first ^= each
        ans = [first]
        for code in encoded:
            ans.append(ans[-1] ^ code)
        return ans


if __name__ == '__main__':
    encoded = [6, 5, 4, 6]
    encoded = [3, 1]
    print(Solution().decode(encoded))
