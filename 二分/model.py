# -*- coding: utf-8 -*-
# @Time    : 2021/4/8 11:30
# @File    : model.py

# https://www.zhihu.com/question/36132386/answer/530313852
def lower_bound(array, lo, hi, target):  # 求非降序范围[lo, hi)内第一个不小于target的值的位置
    while lo < hi:  # 搜索区间[lo, hi)不为空
        mid = lo + (hi - lo) // 2  # 防溢出
        if array[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo  # hi也行，因为[lo, hi)为空的时候它们重合
