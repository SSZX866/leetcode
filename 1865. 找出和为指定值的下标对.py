# -*- coding: utf-8 -*-
# @Time    : 2021/5/16 10:41
# @File    : 5761. 找出和为指定值的下标对.py
from leetcode import *


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        tmp1, tmp2 = [[nums1[i], i] for i in range(len(nums1))], [[nums2[i], i] for i in range(len(nums2))]
        self.nums1 = sorted(tmp1, key=lambda x: x[0])
        self.nums2 = sorted(tmp2, key=lambda x: x[0])

    def add(self, index: int, val: int) -> None:
        for i in range(len(self.nums2)):
            if self.nums2[i][1] == index:
                tmp = self.nums2.pop(i)
                tmp[0] += val
                lo, hi = 0, len(self.nums2)
                while lo < hi:
                    mid = lo + (hi - lo) // 2
                    if self.nums2[mid][0] < tmp[0]:
                        lo = mid + 1
                    else:
                        hi = mid
                self.nums2 = self.nums2[:hi] + tmp + self.nums2[hi:]
            break

    def count(self, tot: int) -> int:
        ans, lo, hi = 0, 0, len(self.nums2) - 1
        while lo < len(self.nums1) and hi >= 0:
            if self.nums1[lo][0] + self.nums2[hi][0] == tot:
                a = b = 1
                while lo + 1 < len(self.nums1) and self.nums1[lo + 1][0] == self.nums1[lo][0]:
                    lo += 1
                    a += 1
                while hi - 1 >= 0 and self.nums2[hi - 1][0] == self.nums2[hi][0]:
                    hi -= 1
                    b += 1
                ans += a * b
            elif self.nums1[lo][0] + self.nums2[hi][0] < tot:
                if lo + 1 < len(self.nums1) and hi - 1 >= 0 and self.nums1[lo + 1][0] - self.nums1[lo][0] > \
                        self.nums2[hi][0] - self.nums2[hi - 1][0]:
                    hi -= 1
                elif lo + 1 < len(self.nums1) and hi - 1 >= 0 and self.nums1[lo + 1][0] - self.nums1[lo][0] <= \
                        self.nums2[hi][0] - self.nums2[hi - 1][0]:
                    lo += 1
                elif lo + 1 >= len(self.nums1):
                    hi -= 1
                elif hi - 1 <= 0:
                    lo += 1
                else:
                    break
            elif self.nums1[lo][0] + self.nums2[hi][0] > tot:
                hi -= 1
        return ans


# 超时
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        self.nums2[index] += val

    def count(self, tot: int) -> int:
        ans, dic = 0, dict()
        for num in self.nums1:
            if tot - num not in dic:
                dic[tot - num] = 1
            else:
                dic[tot - num] += 1
        for num in self.nums2:
            if num in dic:
                ans += dic[num]
        return ans

# 因为nums2范围大，所以根据nums2建立hash表
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.dic = defaultdict(int)
        for num in self.nums2:
            self.dic[num] += 1

    def add(self, index: int, val: int) -> None:
        self.dic[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.dic[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        ans = 0
        for num in self.nums1:
            ans += self.dic[tot - num]
        return ans

# 进一步优化
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        # 初始化两个动态数组
        self.nums1 = nums1
        self.nums2 = nums2
        m, n = len(nums1), len(nums2)
        # 初始化数组出现元素的频率
        self.freq1 = Counter(self.nums1)
        self.freq2 = Counter(self.nums2)
        # 数组1中的元素不变，对其排序后，提前退出降低时间复杂度
        self.key1 = sorted(list(self.freq1.keys()))


    def add(self, index: int, val: int) -> None:
        # 数组2对元素出现频率进行更新
        self.freq2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.freq2[self.nums2[index]] += 1


    def count(self, tot: int) -> int:
        res = 0
        # 在哈希表中查找两数和
        for k in self.key1:
            if (tot - k) in self.freq2:
                res += self.freq1[k] * self.freq2[tot - k]
            if k >= tot:
                break
        return res
