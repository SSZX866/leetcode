# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 23:04
# @File    : 5783. 设计电影租借系统.py
import heapq

from leetcode import *


class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.Rent = []
        self.dic = {}  # dic[电影]：[价格，商店]
        for entry in entries:
            if entry[1] not in self.dic:
                self.dic[entry[1]] = []
            heapq.heappush(self.dic[entry[1]], (entry[2], entry[0]))
        self.entry = {}  # 商店：电影：价格
        for entry in entries:
            if entry[0] not in self.entry:
                self.entry[entry[0]] = {}
            self.entry[entry[0]][entry[1]] = entry[2]

    def search(self, movie: int) -> List[int]:
        ans = []
        if movie not in self.dic: return ans
        tmp = heapq.nsmallest(len(self.dic[movie]), self.dic[movie])
        cnt = 0
        for each in tmp:
            if each[1] not in self.Rent or movie not in self.Rent[each[1]]:
                ans.append(each[1])
                cnt += 1
                if cnt == 5: break
        return ans

    def rent(self, shop: int, movie: int) -> None:
        price = self.entry[shop][movie]
        heapq.heappush(self.Rent, (price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        for i in range(len(self.Rent)):
            if self.Rent[i][1] == shop and self.Rent[i][2] == movie:
                self.Rent.pop(i)
        heapq.heapify(self.Rent)

    def report(self) -> List[List[int]]:
        ans = []
        for each in heapq.nsmallest(5, self.Rent):
            ans.append([each[1], each[2]])
        return ans
