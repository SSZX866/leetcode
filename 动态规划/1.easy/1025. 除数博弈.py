class Solution:
    def divisorGame(self, N: int) -> bool:
        # dp = N * [0]
        # dp[0] = 1
        # for i in range(1, N):
        #     dp[i] = dp[i-1] + 1
        # print(dp)
        # return True
        return N % 2 == 0
if __name__ == '__main__':
    Solution().divisorGame(10)