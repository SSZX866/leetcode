# -*- coding: utf-8 -*-
# @Time    : 2021/7/6 13:14
# @File    : 1418. 点菜展示表.py
from leetcode import *


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        vegetables = set()
        desk = defaultdict(lambda: defaultdict(int))
        for order in orders:
            desk[order[1]][order[2]] += 1
            vegetables.add(order[2])
        # vegetables = sorted(list(vegetables))
        vegetables = sorted(vegetables)  # sorted可以直接转为list
        ans = [['Table'] + vegetables]
        for key in sorted(desk.keys(), key=lambda x: int(x)):
            tmp = [key]
            for vegetable in vegetables:
                tmp.append(str(desk[key][vegetable]))
            ans.append(tmp)
        return ans


if __name__ == '__main__':
    orders = [["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"],
              ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]

    print(Solution().displayTable(orders))
