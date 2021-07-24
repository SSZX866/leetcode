# -*- coding: utf-8 -*-
# @Time    : 2021/07/24 17:13
# @File    : 1736. 替换隐藏数字得到的最晚时间
from leetcode import *


class Solution:
    def maximumTime(self, time: str) -> str:
        if time[0] == '?':
            time = '1' + time[1:] if time[1] != '?' and time[1] > '3' else '2' + time[1:]
        if time[1] == '?':
            time = time[0] + '3' + time[2:] if time[0] == '2' else time[0] + '9' + time[2:]
        if time[3] == '?':
            time = time[:3] + '5' + time[4:]
        if time[4] == '?':
            time = time[:4] + '9'
        return time
