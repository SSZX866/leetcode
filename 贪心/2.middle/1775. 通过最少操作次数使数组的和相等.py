# -*- coding: utf-8 -*-
# @Time    : 2021/5/31 17:49
# @File    : 1775. 通过最少操作次数使数组的和相等.py
from leetcode import *


# 优先队列模拟
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        if (m > n and m > 6 * n) or (m < n and m * 6 < n): return -1
        sum1, sum2 = sum(nums1), sum(nums2)
        if sum1 == sum2: return 0
        # 确保 sum1>sum2, heap2是小顶堆
        if sum1 < sum2:
            sum1, sum2 = sum2, sum1
            nums1, nums2 = nums2, nums1
        # 小技巧：上句可替换为
        # if sum1 > sum2:
        #     return self.minOperations(nums2, nums1)
        heap1, heap2 = [], nums2
        heapq.heapify(heap2)
        ans = 0
        for num in nums1:
            heapq.heappush(heap1, (-num, num))
        while sum1 != sum2:
            if -heap1[0][0] - 1 <= 6 - heap2[0]:
                tmp = heapq.heappop(heap2)
                if sum1 - sum2 > 6 - tmp:
                    sum2 += 6 - tmp
                    heapq.heappush(heap2, 6)
                else:
                    heapq.heappush(heap2, sum1 - sum2 + tmp)
                    sum2 += sum1 - sum2
            else:
                tmp = -heapq.heappop(heap1)[0]
                if sum1 - sum2 > tmp - 1:
                    sum1 -= tmp - 1
                    heapq.heappush(heap1, (-1, 1))
                else:
                    heapq.heappush(heap1, (-(tmp - (sum1 - sum2)), tmp - (sum1 - sum2)))
                    sum1 -= sum1 - sum2
            ans += 1
        return ans


# 不需要模拟，每次贪心最大的就够了
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        if sum1 == sum2:
            return 0
        if sum1 > sum2:
            return self.minOperations(nums2, nums1)

        diff = sum2 - sum1
        freq = Counter(6 - num for num in nums1) + Counter(num - 1 for num in nums2)
        ans = 0

        for i in range(5, 0, -1):
            if diff <= 0:
                break
            for _ in range(freq[i]):
                if diff <= 0:
                    break
                ans += 1
                diff -= i

        return -1 if diff > 0 else ans


if __name__ == '__main__':
    nums1 = [1, 2, 3, 4, 5, 6]
    nums2 = [1, 1, 2, 2, 2, 2]
    # nums1 = [5, 6, 4, 3, 1, 2]
    # nums2 = [6, 3, 3, 1, 4, 5, 3, 4, 1, 3, 4]
    # nums1 = [3,3,2,4,2,6,2]
    # nums2 = [6,2,6,6,1,1,4,6,4,6,2,5,4,2,1]
    print(Solution().minOperations(nums1, nums2))
