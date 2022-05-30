# -*- coding: utf-8 -*-
# @Time    : 2021/12/14 09:42
# @File    : 630. 课程表 III.py
from leetcode import *


# 按结束时间排序，可以保证我们优先考虑加入先结束的课程。
# 在课程塞满的时候，用当前的(如果耗时更短)替换耗时最长的那一个(所以使用优先队列维护时长)，
# 这样做的意义在于我们用更少的时间完成了相同数量的课程，可以保证后面加入更多课程且不可能比原来的方案的课程少。

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        ans, cur, cost = 0, 0, []
        for duration, lastDay in courses:
            if duration > lastDay: continue
            if cur + duration > lastDay:
                if cost and -cost[0] > duration:
                    cur -= -heapq.heappop(cost)
                    cur += duration
                    heapq.heappush(cost, -duration)
                continue
            cur += duration
            heapq.heappush(cost, -duration)
            ans += 1
        return ans


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        pq, t = [], 0
        for duration, lastDay in sorted(courses, key=lambda x: x[1]):
            if t + duration > lastDay and pq and -pq[0] > duration:
                t += heapq.heappop(pq)
            if t + duration <= lastDay:
                heapq.heappush(pq, -duration)
                t += duration
        return len(pq)
