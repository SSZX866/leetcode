# -*- coding: utf-8 -*-
# @Time    : 2021/3/19 15:13
# @File    : 42. 接雨水.py

# dp[i] 表示高度为i层时接到的雨水
# dp[i] = dp[i-1]+i层可以接到水的数量
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        heightMax = max(height)
        if heightMax == 0: return 0
        i, j = 0, len(height) - 1
        while height[i] == 0: i += 1
        while height[j] == 0: j -= 1
        height = height[i:j + 1]
        i, j, res = 0, len(height) - 1, 0
        last = [i, j]
        h = list(set(height))
        h.sort()
        if h[0] == 0: h.pop(0)
        for eachHeight in range(1, heightMax + 1):
            while i != j:
                print(i, j)
                if height[i] < eachHeight:
                    i += 1
                else:
                    if height[j] < eachHeight:
                        j -= 1
                    else:
                        res += (j - i) + 1

                        last[0], last[1] = i, j
                        break
            if i == j:
                res += 1
                i, j = last[0], last[1]
            print(res)
        return res - sum(height)


if __name__ == '__main__':
    height = [2, 0, 2]
    print(Solution().trap(height))
