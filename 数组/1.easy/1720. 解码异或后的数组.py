# -*- coding: utf-8 -*-
# @Time    : 2021/3/29 11:02
# @File    : 1720. 解码异或后的数组.py
from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        for i in range(len(encoded)):
            result.append(encoded[i] ^ result[i])
        return result

if __name__ == '__main__':
    encoded = [6, 2, 7, 3]
    first = 4
    print(Solution().decode(encoded,first))
    [4, 2, 0, 7, 4]