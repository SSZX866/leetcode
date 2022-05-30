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


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in s]
        ans = s[0]
        for i in range(n):
            dp[i][i] = True
        for L in range(2, n + 1):
            # right - left + 1 = L
            for left in range(n):
                right = L + left - 1
                if right >= n: break
                if left + 1 == right:
                    dp[left][right] = s[left] == s[right]
                    if dp[left][right]:
                        ans = max(ans, s[left:right + 1], key=len)
                else:
                    if dp[left + 1][right - 1]:
                        dp[left][right] = s[left] == s[right]
                        if dp[left][right]:
                            ans = max(ans, s[left:right + 1], key=len)
                    else:
                        dp[left][right] = False
        return ans


# 中心扩散
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def center(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        start, length = 0, 1
        for i in range(n):
            for L in range(2):
                left, right = center(i, i + L)
                if right - left + 1 > length:
                    length = right - left + 1
                    start = left
        return s[start:start + length]


if __name__ == '__main__':
    s = "a"
    print(Solution().longestPalindrome(s))
