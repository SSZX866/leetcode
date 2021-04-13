# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 13:27
# @File    : 1684. 统计一致字符串的数目.py
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        for c in allowed:
            words = list(map(lambda x: x.replace(c, ''), words))
        return str(words).count('\'\'')


if __name__ == '__main__':
    allowed = "ab"
    words = ["ad", "bd", "aaab", "baa", "badab"]
    print(Solution().countConsistentStrings(allowed, words))
