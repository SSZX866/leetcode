# -*- coding: utf-8 -*-
# @Time    : 2021/4/4 20:57
# @File    : 781. 森林中的兔子.py
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic = {str(key): answers.count(key) for key in set(answers)}
        print(dic)
        res = 0
        for key in dic:
            if dic[key] != 1:
                if dic[key] >= int(key) + 1:
                    res += (dic[key] // (int(key) + 1)) * (int(key) + 1)
                    if dic[key] % (int(key) + 1):
                        res += int(key) + 1
                else:
                    res += int(key) + 1
            else:
                res += int(key) + 1
        return res


if __name__ == '__main__':
    answers = [2, 2, 0, 2]
    answers = [1, 1, 2]
    answers = [10, 10, 10]
    answers = []

    print(Solution().numRabbits(answers))
