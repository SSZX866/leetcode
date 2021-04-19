# -*- coding: utf-8 -*-
# @Time    : 2021/4/18 10:30
# @File    : 5734. 判断句子是否为全字母句.py
from leetcode import *


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(list(set(sentence))) == 26


if __name__ == '__main__':
    sentence = "leetcode"
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    print(Solution().checkIfPangram(sentence))
