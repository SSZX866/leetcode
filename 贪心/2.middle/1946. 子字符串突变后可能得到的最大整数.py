# -*- coding: utf-8 -*-
# @Time    : 2021/07/26 11:29
# @File    : 1946. 子字符串突变后可能得到的最大整数
from leetcode import *


class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        ans = ''
        i = 0
        flag = False
        while i < len(num):
            tmp = change[int(num[i])]
            if tmp > int(num[i]):
                ans += str(tmp)
                flag = True
            elif tmp == int(num[i]):
                if flag:
                    ans += str(tmp)
                else:
                    ans += num[i]
            else:
                if flag:
                    break
                else:
                    ans += num[i]
            i += 1
        ans += num[i:]
        return ans
