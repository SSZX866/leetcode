# -*- coding: utf-8 -*-
# @Time:    2021/11/16 11:34
# @File:    391. 完美矩形.py
from leetcode import *


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        cnt = collections.defaultdict(int)
        r0, r1, l0, l1 = -100000, -100000, 100000, 100000
        S = 0
        for xi, yi, ai, bi, in rectangles:
            S += (ai - xi) * (bi - yi)
            if xi <= l0 and yi <= l1:
                l0, l1 = xi, yi
            if ai >= r0 and bi >= r1:
                r0, r1 = ai, bi
            for each in ((xi, yi), (ai, bi), (xi, bi), (ai, yi)):
                cnt[each] += 1
                if cnt[each] > 4: return False
        if (r1 - l1) * (r0 - l0) != S: return False
        for each in ((l0, l1), (r0, r1), (l0, r1), (r0, l1)):
            if cnt[each] != 1: return False
            del cnt[each]
        for k in cnt.keys():
            v = cnt[k]
            if v % 2:
                return False
        return True
