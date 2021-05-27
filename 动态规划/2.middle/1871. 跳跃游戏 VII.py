class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [False] * len(s)
        pre = [0] * (len(s)+1)
        dp[0] = True
        pre[1] = 1
        for i in range(1, len(s)):
            if i <= maxJump and s[i] == '0':
                if i >= minJump:
                    # dp[i] = functools.reduce(lambda x, y: x or y, dp[0:i - minJump + 1])
                    dp[i] = (pre[i - minJump+1]) > 0
            elif s[i] == '0':
                # dp[i] = functools.reduce(lambda x, y: x or y, dp[i - maxJump:i - minJump + 1])
                dp[i] = (pre[i - minJump+1] - pre[i - maxJump]) > 0
            pre[i+1] = pre[i] + bool(dp[i])
        # print(pre,dp)
        return dp[-1]