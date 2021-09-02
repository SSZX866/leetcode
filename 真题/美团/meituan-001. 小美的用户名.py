# -*- coding: utf-8 -*-
# @Time    : 2021/8/29 16:59
# @File    : meituan-001. 小美的用户名.py
from leetcode import *

n = int(input())
for i in range(n):
    s = str(input())
    res = 'Accept'
    digit = False
    if not s[0].isalpha():
        res = 'Wrong'
        print(res)
        continue
    for c in s:
        if not c.isdigit() and not c.isalpha():
            res = 'Wrong'
            break
        if c.isdigit(): digit = True
    if not digit:
        res = 'Wrong'
    print(res)
import random