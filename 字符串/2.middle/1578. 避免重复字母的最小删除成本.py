# -*- coding: utf-8 -*-
# @Time    : 2021/3/21 18:34
# @File    : 1578. 避免重复字母的最小删除成本.py
from typing import List

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        index, totalCost = 0, 0
        for i in range(1,len(s)):
            # print(i,index,totalCost)
            if s[i] == s[index]:
                continue
            else:
                if i - index >= 2:
                    totalCost += sum(sorted(cost[index:i])[:i-index-1])
                    # print(cost[index:i],sorted(cost[index:i])[:i-index-1])
                index = i
        if i - index >= 1:
            totalCost += sum(sorted(cost[index:])[:i - index])
        return totalCost

if __name__ == '__main__':
    s = "abaacccac"
    cost = [1,2,3,4,5,7,2,3,1]
    print(Solution().minCost(s,cost))
