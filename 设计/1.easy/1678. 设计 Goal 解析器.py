# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 11:06
# @File    : 1678. 设计 Goal 解析器.py
class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")