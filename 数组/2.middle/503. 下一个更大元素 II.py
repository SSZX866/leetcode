from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1]*len(nums)
        for i in range(len(nums)):
            mark = False
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                  result[i] = nums[j]
                  mark = True
                  break
            if not mark:
                for j in range(i):
                    if nums[j] > nums[i]:
                      result[i] = nums[j]
                      break
        return result

if __name__ == '__main__':
    nums = [1,8,-1,-100,-1,222,1111111,-111111]
    print(Solution().nextGreaterElements(nums))