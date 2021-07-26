# -*- coding: utf-8 -*-
# @Time    : 2021/4/3 19:25
# @File    : 1143. 最长公共子序列.py
from leetcode import *

# 单个数组或者字符串要用动态规划时，可以把动态规划 dp[i] 定义为 nums[0:i] 中想要求的结果；
# 当两个数组或者字符串要用动态规划时，可以把动态规划定义成两维的 dp[i][j]，其含义是在 A[0:i] 与 B[0:j]之间匹配得到的想要的结果。


# dp[i][j] text1前i个和text2前j个匹配的子序列数不包含i，j
# dp[i][j] = dp[i-1][j-1] + 1, i==j
# dp[i][j] = max(dp[i-1][j]，dp[i][j-1]), i!=j

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in text1 + ' ']
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # print(dp)
        return dp[len(text1)][len(text2)]
        # dp = [[0] * (len(text2)) for _ in text1]
        # for i in range(len(text1)):
        #     for j in range(len(text2)):
        #         print(text1[i], text2[j])
        #         if text1[i] == text2[j]:
        #             if i - 1 < 0 or j - 1 < 0:
        #                 dp[i][j] = 1
        #             else:
        #                 dp[i][j] = dp[i - 1][j - 1] + 1
        #         else:
        #             if i - 1 < 0:
        #                 dp[i][j] = dp[i][j - 1]
        #             elif j - 1 < 0:
        #                 dp[i][j] = dp[i - 1][j]
        #             else:
        #                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        #         print(dp)
        # print(dp)
        return dp[-1][-1]

# 字典+二分 o(nlogn)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        hashmap = defaultdict(list)
        for i in range(len(text2) - 1, -1, -1):
            hashmap[text2[i]].append(i)
        indices = []
        for s in text1:
            indices += hashmap[s]
        result = []
        for index in indices:
            insert_index = bisect.bisect_left(result, index)
            if insert_index == len(result):
                result.append(index)
            else:
                result[insert_index] = index
        return len(result)

if __name__ == '__main__':
    text1 = "abcde"
    text2 = "ace"
    print(Solution().longestCommonSubsequence(text1, text2))
