# -*- coding: utf-8 -*-
# @Time    : 2021/10/9 10:16
# @File    : Model.py
from leetcode import *


# 参考 https://zhuanlan.zhihu.com/p/93647900/
class UnionFind:
    def __init__(self, n):
        self.fa = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if x == self.fa[x]:
            return x
        self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def merge(self, x, y):
        i, j = self.find(x), self.find(y)
        # 秩较小的树挂在较大的树上
        if self.rank[i] <= self.rank[j]:
            self.fa[i] = j
        else:
            self.fa[j] = i
        # 只有秩相同的时候需要更新秩
        if self.rank[i] == self.rank[j] and i != j:
            self.rank[j] += 1
