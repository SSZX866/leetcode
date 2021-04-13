# -*- coding: utf-8 -*-
# @Time    : 2021/4/8 11:30
# @File    : model.py
def lower_bound(array, left, right, target):  # 求非降序范围[left, right)内第一个不小于target的值的位置
    while left < right:  # 搜索区间[left, right)不为空
        mid = left + (right - left) // 2  # 防溢出
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left  # right也行，因为[left, right)为空的时候它们重合
