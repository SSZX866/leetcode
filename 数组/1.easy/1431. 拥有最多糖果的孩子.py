# -*- coding: utf-8 -*-
# @Time    : 2021/3/29 10:24
# @File    : 1431. 拥有最多糖果的孩子.py
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [True if extraCandies + candie >= max(candies) else False for candie in candies]

if __name__ == '__main__':
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    print(Solution().kidsWithCandies(candies,extraCandies))
