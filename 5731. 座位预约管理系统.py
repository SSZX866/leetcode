# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 22:37
# @File    : 5731. 座位预约管理系统.py
from leetcode import *


class SeatManager:

    def __init__(self, n: int):
        self.seat = [i+1 for i in range(n)]
        heapq.heapify(self.seat)

    def reserve(self) -> int:
        if self.seat:
            return heapq.heappop(self.seat)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seat, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
