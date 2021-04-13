# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 15:00
# @File    : 1. 蓄水.py
from typing import List


class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        tmp = [v - b for b, v in zip(bucket, vat)]
        print(tmp)
        return max(tmp)+1

if __name__ == '__main__':
    print(Solution().storeWater(bucket=[9, 0, 1], vat=[0, 2, 2]))
    print(Solution().storeWater(bucket = [1,3], vat = [6,8]))
