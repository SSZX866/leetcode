# -*- coding: utf-8 -*-
# @Time    : 2021/9/24 10:49
# @File    : 841. 钥匙和房间.py
from leetcode import *


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        keys = {0}
        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if key not in keys:
                    keys.add(key)
                    stack.append(key)
        return keys == set(range(len(rooms)))
