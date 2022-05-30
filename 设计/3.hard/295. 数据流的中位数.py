# -*- coding: utf-8 -*-
# @Time    : 2021/8/27 12:20
# @File    : 295. 数据流的中位数.py
from leetcode import *


# 二分插入， 数组插入操作耗时多
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._container = []
        self._length = 0

    def addNum(self, num: int) -> None:
        if not self._length:
            self._container.append(num)
        else:
            lo, hi = 0, self._length
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if self._container[mid] < num:
                    lo = mid + 1
                else:
                    hi = mid
            self._container.insert(lo, num)
        self._length += 1

    def findMedian(self) -> float:
        if not self._length: return None
        mid = self._length // 2
        return float(self._container[mid]) if self._length % 2 else (self._container[mid] + self._container[
            mid - 1]) / 2


# 对顶堆，保证大顶堆堆顶小于小顶堆堆顶
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.largeHeap = []
        self.smallHeap = []

    def addNum(self, num: int) -> None:
        # 先放入大顶堆再弹出最大的放入小顶堆，这样可以保证小顶堆堆顶永远大于大顶堆堆顶
        heapq.heappush(self.smallHeap, -heapq.heappushpop(self.largeHeap, -num))
        if len(self.largeHeap) < len(self.smallHeap):
            heapq.heappush(self.largeHeap, -heapq.heappop(self.smallHeap))

    def findMedian(self) -> float:
        if len(self.largeHeap) != len(self.smallHeap): return float(-self.largeHeap[0])
        return (-self.largeHeap[0] + self.smallHeap[0]) / 2


if __name__ == '__main__':
    # def execute(target, f, p):
    #     if f == "addNum":
    #         target.addNum(p[0])
    #         return None
    #     elif f == "findMedian":
    #         # print(obj._container)
    #         return obj.findMedian()
    #     else:
    #         return None

    def execute(target, f, p):
        if f != "MedianFinder":
            return eval("target." + f + '(' + str(p[0]) + ')') if p else eval("target." + f + '()')


    func = ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
            "findMedian",
            "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
            "findMedian", "addNum", "findMedian", "addNum", "findMedian"]
    parameter = [[], [6], [], [10], [], [2], [], [6], [], [5], [], [0], [], [6], [], [3], [], [1], [], [0], [], [0], []]
    func = ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian", "addNum",
            "findMedian", "addNum", "findMedian"]
    parameter = [[], [-1], [], [-2], [], [-3], [], [-4], [], [-5], []]
    obj = MedianFinder()
    res = []
    for i in range(len(func)):
        print(obj.largeHeap)
        print(obj.smallHeap)
        print(i, '-' * 40)
        res.append(execute(obj, func[i], parameter[i]))
    print(res)
