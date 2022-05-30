# -*- coding: utf-8 -*-
# @Time    : 2021/11/24 09:31
# @File    : 423. 从英文中重建数字.py
from leetcode import *


# dic = {
#         'zero': 0, 'one': 1, 'two': 2, 'three': 3,
#         'four': 4, 'five': 5, 'six': 6, 'seven': 7,
#         'eight': 8, 'nine': 9
#         }
# x -> 6
# z -> 0
# s -> 6, 7
# v -> 5, 7
# f -> 4, 5
# r -> 3, 4, 0
# h -> 3, 8
# t -> 2, 3, 8
# i -> 5, 6, 8, 9
# n -> 1, 7, 9
class Solution:
    def originalDigits(self, s: str) -> str:
        dic = collections.defaultdict(int)
        counter = Counter(s)
        dic[6] = counter.get('x', 0)
        dic[0] = counter.get('z', 0)
        dic[7] = counter.get('s', 0) - dic[6]
        dic[5] = counter.get('v', 0) - dic[7]
        dic[4] = counter.get('f', 0) - dic[5]
        dic[3] = counter.get('r', 0) - dic[4] - dic[0]
        dic[8] = counter.get('h', 0) - dic[3]
        dic[2] = counter.get('t', 0) - dic[8] - dic[3]
        dic[9] = counter.get('i', 0) - dic[5] - dic[6] - dic[8]
        dic[1] = counter.get('n', 0) - 2 * dic[9] - dic[7]
        return ''.join(str(k) * dic[k] for k in range(10))


# 简洁代码
class Solution:
    def originalDigits(self, s: str) -> str:
        dic = collections.defaultdict(int)
        counter = Counter(s)
        order = [
            (6, 'x', []), (0, 'z', []), (7, 's', [6]), (5, 'v', [7]),
            (4, 'f', [5]), (3, 'r', [4, 0]), (8, 'h', [3]),
            (2, 't', [8, 3]), (9, 'i', [5, 6, 8]), (1, 'n', [9, 9, 7])]
        for t, c, diff in order:
            dic[t] = counter.get(c, 0) - sum(dic[each] for each in diff)
        return ''.join(str(k) * dic[k] for k in range(10))
