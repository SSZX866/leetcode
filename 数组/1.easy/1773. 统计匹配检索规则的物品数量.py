# -*- coding: utf-8 -*-
# @Time    : 2021/3/29 10:45
# @File    : 1773. 统计匹配检索规则的物品数量.py
from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        dic = {"type": 0, "color": 1, "name": 2}
        return list(zip(*items))[dic[ruleKey]].count(ruleValue)

if __name__ == '__main__':
    items = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"],
             ["phone", "gold", "iphone"]]
    ruleKey = "color"
    ruleValue = "silver"
    print(Solution().countMatches(items,ruleKey,ruleValue))