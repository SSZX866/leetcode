# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 10:38
# @File    : 80. 删除有序数组中的重复项 II.py
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, index, res = 1, 0, len(nums)
        while i < res:
            if nums[i] == nums[i - 1]:
                index = i
                while i < res and nums[i] == nums[i - 1]:
                    i += 1
                if i != index + 1:
                    nums[:] = nums[:index + 1] + nums[i:] + nums[index + 1:i]
                    res -= i - index - 1
                    i -= index
                else:
                    i += 1
            else:
                i += 1
        return res


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    nums = [1, 1, 1, 2, 2, 2, 3, 3]
    nums = [0, 0, 1, 1, 1, 1, 2, 2, 2, 4]
    # nums = [-42,-41,-40,-40,-40,-40,-40,-40,-39,-38,-38,-38,-38,-37]
    # print(Solution().removeDuplicates(list(map(lambda x:x+45,nums))))
    print(Solution().removeDuplicates(nums))
