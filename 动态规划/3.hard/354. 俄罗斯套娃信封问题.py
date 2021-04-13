from typing import List

# 首先我们将所有的信封按照w值第一关键字升序、h值第二关键字降序进行排序；
# 随后我们就可以忽略w维度，求出h维度的最长严格递增子序列，其长度即为答案。

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if envelopes == []:
            return 0
        n = len(envelopes)
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        print(envelopes)
        dp = [1]*n
        for i in range(1,n):
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
        print(dp)
        return max(dp)

# class Solution:
#     def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
#         envelopes.sort(key=lambda x:(x[0],x[1]))
#         cnt = 1
#         pre = envelopes[0]
#         ppp = [pre]
#         print(envelopes)
#         for i in range(1,len(envelopes)):
#             if envelopes[i][0] > pre[0] and envelopes[i][1] > pre[1]:
#                 cnt += 1
#                 pre = envelopes[i]
#                 ppp.append(pre)
#                 print(ppp)
#         return cnt

if __name__ == '__main__':
    envelopes = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
    print(Solution().maxEnvelopes(envelopes))