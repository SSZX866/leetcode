# -*- coding: utf-8 -*-
# @Time    : 2021/11/22 09:02
# @File    : 384. 打乱数组.py
from leetcode import *


# 洗牌算法
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums[:]
        self.resetNums = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.resetNums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        # 从[i, n)中随机选一个填入数组
        # 在0 ~ n-1中随机选一个坐标，将它作为第一个
        # 剩下的n-1个数里，继续随机一个1 ~ n-1的坐标，将它作为第二个，和第二个交换位置，
        # 每次选择的概率均为1 / n  = 前一轮没被选中的概率 * 这一轮被选中的概率 = (n - i / n) * (1 / n - i) = 1 / n
        tmp = self.nums[:]
        for i in range(len(self.nums)):
            j = random.randint(i, len(self.nums) - 1)
            tmp[i], tmp[j] = tmp[j], tmp[i]
        return tmp

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
