# -*- coding: utf-8 -*-
# @Time    : 2021/3/31 21:26
# @File    : 1662. 检查两个字符串数组是否相等.py
from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word = ["", ""]
        for c in word1:
            word[0] += c
        for c in word2:
            word[1] += c
        return word[1] == word[0]
        # return ''.join(word1) == ''.join(word2)

if __name__ == '__main__':
    print(Solution().arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"]))
