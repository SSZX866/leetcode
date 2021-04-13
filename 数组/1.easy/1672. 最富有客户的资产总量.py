# -*- coding: utf-8 -*-
# @Time    : 2021/3/29 10:07
# @File    : 1672. 最富有客户的资产总量.py
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(account) for account in accounts)
