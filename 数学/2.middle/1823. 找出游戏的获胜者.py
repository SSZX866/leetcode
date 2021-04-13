# -*- coding: utf-8 -*-
# @Time    : 2021/4/11 10:35
# @File    : 5727. 找出游戏的获胜者.py
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [i + 1 for i in range(n)]
        i = k - 1
        while n != 1:
            nums.pop(i)
            n = len(nums)
            i = (i + k - 1) % n
        return nums[i]


if __name__ == '__main__':
    print(Solution().findTheWinner(n=6, k=5))
