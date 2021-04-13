# -*- coding: utf-8 -*-
# @Time    : 2021/4/3 23:21
# @File    : 1814. 统计一个数组中好对子的数目.py

from typing import List
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        revNums,res,calc = [],0,[]
        for num in nums:
            revNums.append(int(''.join(reversed(str(num)))))
        for i in range(n):
            calc.append(revNums[i] - nums[i])
        # print(calc,list(set(calc)))
        for each in set(calc):
            if calc.count(each) > 1:
                res += sum([x for x in range(calc.count(each))])
        return res%1000000007
if __name__ == '__main__':
    nums = [42,11,1,97]
    print(Solution().countNicePairs(nums))