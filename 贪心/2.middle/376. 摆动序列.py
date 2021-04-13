from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]):
        """

        :rtype: object
        """
        status = 0 #初始：0 上升：1 下降：-1
        length = len(nums)
        if length < 3:
            return len(set(nums))
        i = 0
        result = []
        while i+1 < length:
            if status == 0:
                if nums[i+1] > nums[i]:
                    status = 1
                    result.append(nums[i])
                elif nums[i+1] < nums[i]:
                    status = -1
                    result.append(nums[i])
                i += 1
            elif status == 1:
                while i+1 < length:
                    if nums[i+1] >= nums[i]:
                        i += 1
                    else:
                        print(1111,nums[i])
                        result.append(nums[i])
                        i += 1
                        break
                if i+1 == length:
                    if nums[i] < nums[i-1]:
                        result.append(nums[i])
                        return len(result), result,111
                else:
                    status = -1
            else:
                while i + 1 < length:
                    print(2222, nums[i])
                    if nums[i + 1] <= nums[i]:
                        i += 1
                    else:
                        result.append(nums[i])
                        i += 1
                        break
                if i+1 == length:
                    if nums[i] > nums[i - 1]:
                        result.append(nums[i])
                        return len(result), result,222
                else:
                    status = 1
            print(i,status)
        if i + 1 == length:
            result.append(nums[i])
        return len(result), result,333
if __name__ == '__main__':
    nums = [1,7,4,9,2,5]
    print(Solution().wiggleMaxLength(nums))