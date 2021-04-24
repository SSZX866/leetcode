# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 16:17
# @File    : 记忆化搜索.py
from leetcode import *
import time
from functools import lru_cache


def search(n, f):
    if n < 2:
        f[n] = 1
    elif f[n] == 0:
        f[n] = search(n - 1, f) + search(n - 2, f)
    return f[n]


def recur(n):
    if n < 2: return 1
    return recur(n - 1) + recur(n - 2)

@lru_cache(None)
def recur(n):
    if n < 2: return 1
    return recur(n - 1) + recur(n - 2)


t1 = time.time()
print(search(35, [0] * 36))
t2 = time.time()
print(recur(35))
print(t2 - t1, time.time() - t2)
