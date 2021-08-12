from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]):
        """

        :rtype: object
        """
        status = 0  # 初始：0 上升：1 下降：-1
        length = len(nums)
        if length < 3:
            return len(set(nums))
        i = 0
        result = []
        while i + 1 < length:
            if status == 0:
                if nums[i + 1] > nums[i]:
                    status = 1
                    result.append(nums[i])
                elif nums[i + 1] < nums[i]:
                    status = -1
                    result.append(nums[i])
                i += 1
            elif status == 1:
                while i + 1 < length:
                    if nums[i + 1] >= nums[i]:
                        i += 1
                    else:
                        print(1111, nums[i])
                        result.append(nums[i])
                        i += 1
                        break
                if i + 1 == length:
                    if nums[i] < nums[i - 1]:
                        result.append(nums[i])
                        return len(result), result, 111
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
                if i + 1 == length:
                    if nums[i] > nums[i - 1]:
                        result.append(nums[i])
                        return len(result), result, 222
                else:
                    status = 1
            print(i, status)
        if i + 1 == length:
            result.append(nums[i])
        return len(result), result, 333


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dp = [[0] * 2 for _ in nums]
        dp[0][0] = dp[0][1] = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                dp[i][0] = dp[i - 1][1] + 1  # 下降
            else:
                dp[i][0] = dp[i - 1][0]
            if nums[i] > nums[i - 1]:
                dp[i][1] = dp[i - 1][0] + 1  # 上升
            else:
                dp[i][1] = dp[i - 1][1]
        return max(dp[-1])


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        p = q = 1  # 上升，下降p,q
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                p = q + 1
            if nums[i] < nums[i - 1]:
                q = p + 1
        return max(p, q)


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        dp = [[0] * 2 for _ in nums]
        dp[0] = [1, 1]
        ans = 0
        for i in range(1, len(nums)):
            dp[i][0] = dp[i - 1][1] + 1 if nums[i] > nums[i - 1] else dp[i - 1][0]
            dp[i][1] = dp[i - 1][0] + 1 if nums[i] < nums[i - 1] else dp[i - 1][1]
            ans = max(ans, dp[i][0], dp[i][1])
        return ans


if __name__ == '__main__':
    nums = [1, 7, 4, 9, 2, 5]
    print(Solution().wiggleMaxLength(nums))
