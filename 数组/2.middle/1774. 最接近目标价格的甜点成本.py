# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 11:38
# @File    : 1774. 最接近目标价格的甜点成本.py
from leetcode import *


# 回溯
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        ans = []

        def backtrack(path, index, times):
            tmp = sum(path)
            if tmp not in ans:
                ans.append(tmp)

            for i in range(index, len(toppingCosts)):
                path.append(toppingCosts[i])
                backtrack(path, i + 1, 0) if times else backtrack(path, i, times + 1)
                path.pop()
                times = 0

        backtrack([], 0, 0)
        ans1 = []
        for base in baseCosts:
            for each in ans:
                ans1.append(each + base)
        ans1.sort()
        index = bisect.bisect_left(ans1, target)
        if index == len(ans1): return ans1[-1]
        if index == 0 or ans1[index] == target: return ans1[index]
        return ans1[index] if abs(ans1[index] - target) < abs(ans1[index - 1] - target) else ans1[index - 1]


# 剪枝
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        ans = []

        def backtrack(path, index, times, flag):
            tmp = sum(path)
            if tmp not in ans:
                ans.append(tmp)

            for i in range(index, len(toppingCosts)):
                if flag:
                    continue
                if sum(path) > target:
                    flag = True
                path.append(toppingCosts[i])
                backtrack(path, i + 1, 0, flag) if times else backtrack(path, i, times + 1, flag)
                path.pop()
                flag = False
                times = 0

        backtrack([], 0, 0, False)
        ans1 = []
        for base in baseCosts:
            for each in ans:
                ans1.append(each + base)
        ans1.sort()
        index = bisect.bisect_left(ans1, target)
        if index == len(ans1): return ans1[-1]
        if index == 0 or ans1[index] == target: return ans1[index]
        return ans1[index] if abs(ans1[index] - target) < abs(ans1[index - 1] - target) else ans1[index - 1]


if __name__ == '__main__':
    baseCosts = [1, 7]
    toppingCosts = [3, 4]
    target = 10
    baseCosts = [10]
    toppingCosts = [1]
    target = 1
    baseCosts = [6777, 9, 9570, 9441, 6721, 1907]
    toppingCosts = [9515, 8611, 4005, 5228, 2045, 6488, 3971, 5585, 5223, 2557]
    target = 9650

    print(Solution().closestCost(baseCosts, toppingCosts, target))
