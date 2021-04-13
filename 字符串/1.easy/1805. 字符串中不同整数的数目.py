# -*- coding: utf-8 -*-
# @Time    : 2021/3/28 10:34
# @File    : 5713. 字符串中不同整数的数目.py

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        n, i, j, nums = len(word), 0, 0, []
        word += 'a'
        while i < n:
            j = i
            while ord('0') <= ord(word[j]) <= ord('9'):
                j += 1
            if j != i:
                nums.append(int(word[i:j]))
                i = j
            i += 1
        return len(set(nums))

if __name__ == '__main__':
    word = "a123bc34d8ef34"
    print(Solution().numDifferentIntegers(word))