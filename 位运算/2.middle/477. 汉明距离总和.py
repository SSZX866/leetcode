# -*- coding: utf-8 -*-
# @Time    : 2021/5/28 10:13
# @File    : 477. 汉明距离总和.py
from leetcode import *

# 暴力超时
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        def HammingDistance(a, b):
            tmp, cnt = a ^ b, 0
            while tmp:
                if tmp & 1:
                    cnt += 1
                tmp >>= 1
            return cnt

        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                ans += HammingDistance(nums[i], nums[j])
        return ans

# 乘法原理
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        tmp, n, ans = [], len(nums), 0
        for i in range(30):
            tmp.append(0)
            for j in range(n):
                bit = (nums[j] >> i) & 1
                if bit:
                    tmp[-1] += 1
            ans += tmp[-1]*(n-tmp[-1])
        # ans = 0
        # for each in tmp:
        #     ans += each * (n - each)
        return ans

# 关于format
# 将十进制转换为固定长度的多进制类型：
#
# 8位二进制
# '{:08b}'.format(9)
# '00001001'
#
# 6位8进制
# '{:06o}'.format(9)
# '000011'
#
# 6位16进制
# '{:06x}'.format(9)
# '000009'