# -*- coding: utf-8 -*-
# @Time    : 2021/4/5 16:06
# @File    : LCP30. 魔塔游戏.py
from typing import List


class Solution:
    def magicTower(self, nums: List[int]) -> int:
        if sum(nums) < 0: return -1
        hp = 1
        res = 0
        maxHp, damages = 0, []
        for num in nums:
            hp += num
            if num < 0:
                damages.append(-num)
            if hp <= 0:
                damages.sort()
                damage = damages.pop()
                hp += damage
                nums.append(-damage)
                res += 1
            print(hp,damages,res)
        return res


if __name__ == '__main__':
    print(Solution().magicTower(nums=[-1,-1,10]))
