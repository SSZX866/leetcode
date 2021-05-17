# -*- coding: utf-8 -*-
# @Time    : 2021/5/14 17:50
# @File    : 169. 多数元素.py
from leetcode import *


# 摩尔投票法：

# 从第一个数开始count=1，遇到相同的就加1，遇到不同的就减1，减到0就重新换个数开始计数，总能找到最多的那个

# 核心就是对拼消耗。
# 比如玩一个诸侯争霸的游戏，假设你方人口超过总人口一半以上，并且能保证每个人口出去干仗都能一对一同归于尽。
# 最后还有人活下来的国家就是胜利。
# 那就大混战呗，最差所有人都联合起来对付你（对应你每次选择作为计数器的数都是众数），
# 或者其他国家也会相互攻击（会选择其他数作为计数器的数），但是只要你们不要内斗，最后肯定你赢。
# 最后能剩下的必定是自己人。

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for num in nums:
            dic[str(num)] += 1
        return int(max(dic, key=dic.get))


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, pre = 0, nums[0]
        for num in nums[1:]:
            if num == pre:
                count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    pre = num
                    count = 0
        return pre


if __name__ == '__main__':
    print(Solution().majorityElement([3, 2, 3]))
