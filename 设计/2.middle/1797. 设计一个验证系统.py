# -*- coding: utf-8 -*-
# @Time    : 2021/5/26 20:08
# @File    : 1797. 设计一个验证系统.py
from leetcode import *


class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.task = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.task[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.task:
            if currentTime < self.task[tokenId]:
                self.task[tokenId] = currentTime + self.timeToLive
            else:
                del self.task[tokenId]

    def countUnexpiredTokens(self, currentTime: int) -> int:
        cnt = 0
        for key in list(self.task.keys()):
            # for key in self.task: 修改字典key时不能遍历字典键值
            if self.task[key] > currentTime:
                cnt += 1
            else:
                del self.task[key]
        return cnt
