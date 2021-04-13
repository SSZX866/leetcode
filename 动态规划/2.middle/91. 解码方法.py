
# dp[i] = dp[i-1] + 1 + check(s[i-1:i+1])
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        dp = [0] * n
        dp[0] = 1
        if n > 1:
            if int(s[0]+s[1]) <= 26 and s[1] != '0':
                dp[1] = 2
            elif s[1] == '0' and int(s[0]+s[1]) > 26:
                dp[1] = 0
            else:
                dp[1] = 1
            print(dp)
            for i in range(2,n):
                if s[i] == '0':
                    if s[i-1] == '1' or s[i-1] == '2':
                        dp[i] = dp[i-2]
                    else:
                        return 0
                elif s[i-1] == '1':
                    #s[i-1]和s[i]分开译码为dp[i-1]合并译码为dp[i-2]
                    dp[i] = dp[i-1]+dp[i-2]
                elif s[i-1] == '2':
                    if '1' <= s[i] <= '6':
                        dp[i] = dp[i - 1] + dp[i - 2]
                    else:
                        dp[i] = dp[i - 1]
                else:
                    dp[i] = dp[i - 1]
            print(dp)
        return dp[-1]

if __name__ == '__main__':
    s = "10"
    print(Solution().numDecodings(s))