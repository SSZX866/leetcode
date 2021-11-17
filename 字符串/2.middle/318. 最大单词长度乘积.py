# -*- coding: utf-8 -*-
# @Time    : 2021/11/17 09:00
# @File    : 318. 最大单词长度乘积.py
from leetcode import *


# 集合运算
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        sets = []
        for word in words:
            sets.append(set(word))
        ans = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not (sets[i] & sets[j]):
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans


# 位运算状态压缩
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        dic = {chr(v + ord('a')): v for v in range(26)}
        bits = []
        for i in range(len(words)):
            tmp = 0
            for c in words[i]:
                tmp |= 1 << dic[c]
            bits.append(tmp)
        ans = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not (bits[i] & bits[j]):
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans


# 继续优化
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        dic = {chr(v + ord('a')): v for v in range(26)}
        # 相同词频保存在哈希表中，减少重复运算
        bitDic = collections.defaultdict(int)
        ans = 0
        for i in range(len(words)):
            tmp = 0
            for c in words[i]:
                tmp |= 1 << dic[c]
            if bitDic[tmp] < len(words[i]):
                for k, v in bitDic.items():
                    if not tmp & k:
                        ans = max(ans, v * len(words[i]))
                bitDic[tmp] = max(bitDic[tmp], len(words[i]))
        return ans
