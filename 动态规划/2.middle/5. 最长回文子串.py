# dp[i][j] 表示到第i到j是否为回文串
# dp[i][j] = dp[i+1][j-1] and (s[i]==s[j])
# if i == j: dp[i][j] = True
# elif abs(i-j) == 1: dp[i][j] = (s[i]==s[j])
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        # for i in range(n):
        #     for j in range(i,n):
        #         if i == j:
        #             dp[i][j] = True
        #         elif j - i == 1:
        #             dp[i][j] = (s[i] == s[j])
        # index = [0, 0]
        # for i in range(n):
        #     for j in range(i,n):
        #         if i == j:
        #             dp[i][j] = True
        #         elif j - i == 1:
        #             dp[i][j] = (s[i] == s[j])
        #         elif j - i > 1:
        #             dp[i][j] = dp[i + 1][j-1] and (s[i] == s[j])
        #             print(i, j, 111, dp[i + 1][j-1], (s[i] == s[j]), dp[i][j])
        #         if dp[i][j] and (j-i) > index[1]-index[0]:
        #             index = [i,j]
        index = [0, 0]
        for l in range(n):
            for i in range(n):
                j = i + l
                if j == n:
                    break
                if i == j:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
                if dp[i][j] and (j - i) > index[1] - index[0]:
                    index = [i, j]
        # index = [0,0]
        # for i in range(n):
        #     for j in range(i,n):
        #         if dp[i][j] and (j-i) > index[1]-index[0]:
        #             index = [i,j]
        # print(dp,index)
        print(dp)
        return s[index[0]:index[1] + 1]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2: return s
        dp = [[False] * n for _ in s]
        for i in range(n):
            dp[i][i] = True
        max_len, start = 1, 0
        # 长度 L
        for L in range(2, n + 1):
            # 左边界i
            for i in range(n):
                # 右边界 j - i + 1 = L
                j = L + i - 1
                if j >= n:
                    break
                if s[i] != s[j]:
                    continue
                if L <= 3:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and L > max_len:
                    start = i
                    max_len = L
        return s[start:start + max_len]


if __name__ == '__main__':
    s = "a"
    print(Solution().longestPalindrome(s))
