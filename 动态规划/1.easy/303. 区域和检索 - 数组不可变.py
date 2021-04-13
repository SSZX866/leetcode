from typing import List
"""
【状态定义】
dp[i]为坐标[0, i]的元素总和

【转移方程】
dp[i] = dp[i-1] + nums[i]

【初始值】
dp[0] = nums[0]

【返回值】
i > 0: dp[j] - dp[i-1]
i == 0: dp[j]
"""
class NumArray:
    def __init__(self, nums: List[int]):
        if len(nums)!=0:
            self.dp = [0 for x in range(len(nums))]
            self.dp[0] = nums[0]
            # for i, num in enumerate(nums[1:]):
            #     self.dp[i+1] = num + self.dp[i]
            for i in range(1, len(nums)):
                self.dp[i] = self.dp[i - 1] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        if i != 0:
            return self.dp[j] - self.dp[i-1]
        else:
            return self.dp[j]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)