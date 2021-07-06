# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 15:20
# @File    : 726. 原子的数量.py
import time

from leetcode import *


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        i = 0
        stack = []
        tmp = defaultdict(int)
        tmpStr = ''
        while i < len(formula):
            if formula[i] == '(':
                stack.append(tmp)
                tmp = defaultdict(int)
            elif formula[i] == ')':
                dic = stack.pop()
                nums = ''
                while i + 1 < len(formula) and formula[i + 1] in '0123456789':
                    i += 1
                    nums += formula[i]
                if nums:
                    for key in tmp.keys():
                        tmp[key] *= int(int(nums))
                for key in dic.keys():
                    tmp[key] += dic[key]
            else:
                if 64 < ord(formula[i]) < 91:
                    tmpStr += formula[i]
                    i += 1
                while i < len(formula) and 123 > ord(formula[i]) > 96:
                    tmpStr += formula[i]
                    i += 1
                i -= 1
                nums = ''
                while i + 1 < len(formula) and formula[i + 1] in '0123456789':
                    i += 1
                    nums += formula[i]
                tmp[tmpStr] = tmp[tmpStr] + int(nums) if nums else tmp[tmpStr] + 1
                tmpStr = ''
            i += 1

        ans = ''
        for key in sorted(tmp.keys()):
            ans += key + str(tmp[key]) if tmp[key] > 1 else key

        return ans


if __name__ == '__main__':
    formula = "H2O"
    formula = "Mg(OH)2"
    formula = "K4(ON(SO3)2)2"
    formula = "Be32"
    formula = "H50"
    print(Solution().countOfAtoms(formula))
