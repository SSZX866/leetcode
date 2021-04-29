# -*- coding: utf-8 -*-
# @Time    : 2021/4/29 18:20
# @File    : 403. 青蛙过河.py
import functools

from leetcode import *


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [-1] * n
        dp[1] = 1
        for i in range(2, n):
            mark = False
            for j in range(1, i):
                tmp = stones[i] - dp[j]
                if abs(tmp - dp[i - 1]) <= 1:
                    mark = True
                    break
            if not mark: return False
            dp[i] = dp[i - 1] + tmp
            print(tmp, dp)
        print(dp)
        return dp[-1] != -1


class Solution:
    def canCross(self, stones: List[int]) -> bool:

        if stones[1] - stones[0] > 1: return False

        stonesSet = set(stones)  # 变成Set， 加速检索

        @functools.lru_cache(None)  # 加上备忘录，去掉重复计算
        def helper(i, step):
            # 状态，表示当前是第几块石头，是走几步走过来的。
            if i == stones[-1]:
                return True

            # 选择， 走 step + 1 步， 走 step 步，还是走step - 1 步？，
            # 只要往前走的步数有石头（在数组内），就试着可以往前走
            if i + step + 1 in stonesSet:
                if helper(i + step + 1, step + 1):
                    return True

            if i + step in stonesSet:
                if helper(i + step, step):
                    return True

            if step - 1 > 0 and i + step - 1 in stonesSet:
                # 这边要检查一下，step -1 要大于0 才走
                if helper(i + step - 1, step - 1):
                    return True

            return False

        return helper(stones[1], stones[1] - stones[0])

if __name__ == '__main__':
    stones = [0, 1, 3, 5, 6, 8, 12, 17]
    # stones = [0, 1, 2, 3, 4, 8, 9, 11]
    print(Solution().canCross(stones))
