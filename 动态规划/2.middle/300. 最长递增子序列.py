from typing import List

# o（n^2)
# dp[i] 从前i个元素，以第i个 数 字 结 尾 的最长上升子序列的长度
# dp[i] = max(dp[j]) + 1 0<j<i nums[j]<nums[i]
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j] + 1)
        return max(dp)


# o(nlogn) 二分
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d)

if __name__ == '__main__':
    nums = [0,1,0,3,2,3]
    print(Solution().lengthOfLIS(nums))