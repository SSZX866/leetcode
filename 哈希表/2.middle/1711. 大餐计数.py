# -*- coding: utf-8 -*-
# @Time    : 2021/7/7 11:12
# @File    : 1711. 大餐计数.py
from leetcode import *


# 暴力超时
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        def checkBin(target):
            flag = False
            for i in range(22):
                if target & 1: flag = True
                target = target >> 1
                if flag:
                    return not target

        deliciousness.sort()
        dic = defaultdict(int)
        i, j = 0, 0
        while i < len(deliciousness):
            while j < len(deliciousness):
                j += 1
                if j < len(deliciousness):
                    meal = deliciousness[j] + deliciousness[i]
                    if dic[meal] or checkBin(meal):
                        dic[meal] += 1
            i += 1
            j = i

        ans = 0
        for key in dic.keys():
            ans += dic[key]

        return ans


# hash 进阶版两数之和
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        def editDic(target):
            base = 0
            for i in range(22):
                if not base:
                    base = 1
                else:
                    base <<= 1
                if target <= base:
                    dic[base - target] += 1

        dic = defaultdict(int)
        ans = 0
        for each in deliciousness:
            ans += dic[each]
            editDic(each)
        return ans % 1000000007

if __name__ == '__main__':
    deliciousness = [1, 3, 5, 7, 9]
    deliciousness = [1, 1, 1, 3, 3, 3, 7]
    deliciousness = [149, 107, 1, 63, 0, 1, 6867, 1325, 5611, 2581, 39, 89, 46, 18, 12, 20, 22, 234]
    deliciousness = [1048576, 1048576]
    print(Solution().countPairs(deliciousness))
