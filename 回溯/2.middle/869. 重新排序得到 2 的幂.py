# -*- coding: utf-8 -*-
# @Time    : 2021/10/28 10:24
# @File    : 869. 重新排序得到 2 的幂.py
from leetcode import *


# 超时
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        length = 0
        tmp, nums = n, []
        while tmp:
            nums.append(tmp % 10)
            tmp //= 10
            length += 1

        indexs = []

        def backtrack(target, path):
            if len(path) == length:
                indexs.append(path[:])
                return
            for val, used in target:
                if not used:
                    path.append(val)
                    target[val][1] = True
                    backtrack(target, path)
                    target[val][1] = False
                    path.pop()

        backtrack([[i, False] for i in range(length)], [])

        def checkBin(target):
            while target and target & 1 ^ 1:
                target >>= 1
            target >>= 1
            return not target

        for index in indexs:
            # 去前导0
            if not nums[index[0]]: continue
            num = 0
            for i in index:
                num += nums[i]
                num *= 10
            num //= 10
            if checkBin(num):
                print(num)
                return True
        return False


# 优化 通过
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        length = 0
        tmp, nums = n, []
        while tmp:
            nums.append(tmp % 10)
            tmp //= 10
            length += 1

        def checkBin(target):
            while target and target & 1 ^ 1:
                target >>= 1
            target >>= 1
            return not target

        def backtrack(target, path):
            if len(path) == length:
                if not nums[path[0]]: return False
                num = 0
                for i in path:
                    num += nums[i]
                    num *= 10
                num //= 10
                if checkBin(num):
                    return True
                return False
            for val, used in target:
                if not used:
                    path.append(val)
                    target[val][1] = True
                    if backtrack(target, path): return True
                    target[val][1] = False
                    path.pop()
            return False

        return backtrack([[i, False] for i in range(length)], [])


# 直接对目标二进制和n排序（这里统计出现数量也可以）比较是否相等
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        tmp = 1
        while tmp < 10 ** 9 + 1:
            if sorted(str(n)) == sorted(str(tmp)):
                return True
            tmp <<= 1
        return False
