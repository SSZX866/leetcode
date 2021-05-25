# -*- coding: utf-8 -*-
# @Time    : 2021/5/25 10:46
# @File    : 1787. 使所有区间的异或结果为零.py
from leetcode import *


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        def helpF(nums, n):
            pre = [0]
            ans = []
            for i in range(n):
                if i < k - 1:
                    ans.append(nums[i])
                else:
                    ans.append(pre[i] ^ pre[i - k + 1])
                pre.append(pre[-1] ^ ans[i])
            return ans

        def helpFReverse(nums, n):
            ans = []
            pre = [0]
            for i in range(n - 1, -1, -1):
                if n - i < k:
                    ans.append(nums[i])
                else:
                    ans.append(pre[n - i - 1] ^ pre[n - i - k])
                pre.append(pre[-1] ^ ans[n - i - 1])
            return ans[::-1]

        def cntDiff(nums1, nums2, n):
            cnt = 0
            for i in range(n):
                if nums1[i] != nums2[i]:
                    cnt += 1
            return cnt

        n = len(nums)
        ans = 2001
        for start in range(n - k + 2):

            i, j = start - 1, start
            tmp = [0] * n
            target = [0]
            while j - start < k - 1:
                tmp[j] = nums[j]
                target[0] ^= tmp[j]
                target.append(tmp[j])
                j += 1

            target = target[1:] + [target[0]]
            targetLen = len(target)
            p, q = targetLen - 1, targetLen - 1
            while i >= 0 or j < n:
                if i >= 0:
                    tmp[i] = target[p]
                    p = (p - 1) % targetLen
                    i -= 1
                if j < n:
                    tmp[j] = target[q]
                    q = (q + 1) % targetLen
                    j += 1
            print(tmp)
            ans = min(ans, cntDiff(nums, tmp, n))

        return ans


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        # x 的范围为 [0, 2^10)
        MAXX = 2 ** 10

        n = len(nums)
        f = [float("inf")] * MAXX
        # 边界条件 f(-1,0)=0
        f[0] = 0

        for i in range(k):
            # 第 i 个组的哈希映射
            count = Counter()
            size = 0
            for j in range(i, n, k):
                count[nums[j]] += 1
                size += 1

            # 求出 t2
            t2min = min(f)

            g = [t2min] * MAXX
            for mask in range(MAXX):
                # t1 则需要枚举 x 才能求出
                for x, countx in count.items():
                    g[mask] = min(g[mask], f[mask ^ x] - countx)

            # 别忘了加上 size
            f = [val + size for val in g]
        return int(f[0])


if __name__ == '__main__':
    nums = [3, 4, 5, 2, 1, 7, 3, 4, 7]
    nums = [1, 2, 4, 1, 2, 5, 1, 2, 6]
    k = 3
    # nums = [1, 2, 0, 3, 0]
    # k = 1
    nums = [26, 19, 19, 28, 13, 14, 6, 25, 28, 19, 0, 15, 25, 11]
    k = 3
    nums = [11, 20, 3, 18, 26, 30, 20, 7, 3, 0, 25, 9, 19, 21, 3, 23]
    k = 5
    print(Solution().minChanges(nums, k))
