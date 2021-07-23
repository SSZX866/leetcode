# -*- coding: utf-8 -*-
# @Time    : 2021/07/23 16:48
# @File    : 1286. 字母组合迭代器
from leetcode import *


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = sorted(characters)
        self.combinationLength = combinationLength

        def backtrack(i, path, tmp):
            if len(path) == self.combinationLength:
                tmp.append(''.join(path))
                return
            for i in range(i, len(self.characters)):
                path.append(self.characters[i])
                backtrack(i + 1, path, tmp)
                path.pop()

        self.tmp = []
        backtrack(0, [], self.tmp)
        self.cur = 0
        self.length = len(self.tmp)

    def next(self) -> str:
        if self.cur < self.length:
            self.cur += 1
            return self.tmp[self.cur - 1]

    def hasNext(self) -> bool:
        return self.cur < self.length
