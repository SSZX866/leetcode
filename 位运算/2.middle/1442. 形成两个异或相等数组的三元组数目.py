# -*- coding: utf-8 -*-
# @Time    : 2021/5/18 10:32
# @File    : 1442. 形成两个异或相等数组的三元组数目.py
from leetcode import *


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        pre, n, scope, ans = [0], len(arr), [], 0
        for i in range(n):
            pre.append(pre[-1] ^ arr[i])
        for i in range(n + 1):
            for k in range(i + 1, n + 1):
                if pre[k] ^ pre[i] == 0:
                    # scope.append([i, k])
                    ans += k-i-1
        # for each in scope:
        #     for j in range(each[0]+1, each[1]):
        #         # print(j,each,pre[each[0]] ^ pre[j],pre[j + 1] ^ pre[each[1]])
        #         if pre[each[0]] ^ pre[j] == pre[j] ^ pre[each[1]]:
        #             print(each[0], j, each[1]-1)
        #             ans += 1
        return ans


if __name__ == '__main__':
    arr = [2, 3, 1, 6, 7]
    arr = [1, 1, 1, 1, 1]
    arr = [7, 11, 12, 9, 5, 2, 7, 17, 22]
    arr = [1, 3, 5, 7, 9]
    arr = [2, 3]
    print(Solution().countTriplets(arr))
