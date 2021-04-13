# -*- coding: utf-8 -*-
# @Time    : 2021/3/29 13:38
# @File    : 1108. IP 地址无效化.py
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', "[.]")
