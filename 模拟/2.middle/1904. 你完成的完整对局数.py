# -*- coding: utf-8 -*-
# @Time    : 2021/6/20 10:44
# @File    : 5789. 你完成的完整对局数.py
from leetcode import *


class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        startTime = startTime.split(':')
        finishTime = finishTime.split(':')

        def calcMin(start, finish):
            start, finish = int(start), int(finish)
            ans = 0
            if start == 0:
                if finish < 15:
                    ans = 0
                elif 15 <= finish < 30:
                    ans = 1
                elif 30 <= finish < 45:
                    ans = 2
                elif 45 <= finish < 60:
                    ans = 3
                else:
                    ans = 4
            elif 0 < start <= 15:
                if finish < 15:
                    ans = 0
                elif 15 <= finish < 30:
                    ans = 0
                elif 30 <= finish < 45:
                    ans = 1
                elif 45 <= finish < 60:
                    ans = 2
                else:
                    ans = 3
            elif 15 < start <= 30:
                if finish < 30:
                    ans = 0
                elif 30 <= finish < 45:
                    ans = 0
                elif 45 <= finish < 60:
                    ans = 1
                else:
                    ans = 2
            elif 30 < start <= 45:
                if finish < 45:
                    ans = 0
                elif 45 <= finish < 60:
                    ans = 0
                else:
                    ans = 1
            else:
                ans = 0
            return ans

        if startTime[0] < finishTime[0]:
            # if startTime[1] < finishTime[1]:
            #     hour = (int(finishTime[0]) - int(startTime[0])) * 4
            #     m = calcMin(startTime[1], finishTime[1])
            # else:
            hour = (int(finishTime[0]) - int(startTime[0]) - 1) * 4
            m = calcMin(startTime[1], 60)
            m += calcMin(0, finishTime[1])
            ans = hour + m
        elif startTime[0] == finishTime[0]:
            if startTime[1] < finishTime[1]:
                hour = (int(finishTime[0]) - int(startTime[0])) * 4
                m = calcMin(startTime[1], finishTime[1])
            else:
                hour = 23 * 4
                m = calcMin(startTime[1], 60)
                m += calcMin(0, finishTime[1])
            ans = hour + m
        else:
            # if startTime[1] <= finishTime[1]:
            #     hour = (24 - int(startTime[0]) + int(finishTime[0])) * 4
            #     m = calcMin(startTime[1], finishTime[1])
            #     print(m, hour)
            # else:
            hour = (24 - int(startTime[0]) + int(finishTime[0]) - 1) * 4
            m = calcMin(startTime[1], 60)
            m += calcMin(0, finishTime[1])
            ans = hour + m
        return ans


if __name__ == '__main__':
    startTime = "00:01"
    finishTime = "00:00"
    startTime = "18:51"
    finishTime = "04:54"
    startTime = "00:01"
    finishTime = "10:01"
    startTime = "13:53"
    finishTime = "16:58"

    print(Solution().numberOfRounds(startTime, finishTime))
