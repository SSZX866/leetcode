# -*- coding: utf-8 -*-
# @Time    : 2021/4/28 16:46
# @File    : 面试题 08.09. 括号.py
from leetcode import *
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrace(path,res,n):
            for i in range(n):
                path.append()