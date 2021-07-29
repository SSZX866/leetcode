from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        i = 0
        nums[-1] = 1
        while i < len(nums):
            if 0 == nums[i]:
                return False
            indexs = []
            while i < len(nums) and nums[i] != 0:
                indexs.append(i + nums[i])
                i += 1
            i_ = i
            for j in range(i, max(indexs) + 1):
                if j >= len(nums):
                    return True
                if nums[j] > nums[i_]:
                    i_ = j
            i = i_
            if i < len(nums) and nums[i] == 0:
                return False
        return True


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = 0
        for i in range(len(nums)):
            if maxJump < i: return False
            maxJump = max(maxJump, i + nums[i])
        return True


if __name__ == '__main__':
    nums = [2, 0, 0]
    print(Solution().canJump(nums))
