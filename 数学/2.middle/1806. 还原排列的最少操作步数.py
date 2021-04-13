# -*- coding: utf-8 -*-
# @Time    : 2021/3/28 11:04
# @File    : 1806. 还原排列的最少操作步数.py
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        # perm, arr = [i for i in range(n)], []
        # for i in range(n):
        #     if i % 2 == 0:
        #         arr.append(perm[int(i / 2)])
        #     else:
        #         arr.append(perm[int(n / 2 + (i - 1) / 2)])
        num = n - 2
        pre = 1
        cnt = 0
        if n == 1: return 0
        while num != 1 and num != n-3:
            if num % 2 == 0:
                num = num / 2
                pre += num
            else:
                pre /= 2
                num += pre
            # print(pre, num, cnt)
            cnt += 1
        if num == n-3: return cnt + 1
        return cnt * 2

if __name__ == '__main__':
    print(Solution().reinitializePermutation(10))
