# -*- coding: utf-8 -*-
# @Time    : 2021/4/11 11:28
# @File    : 5729. 求出 MK 平均值.py
class MKAverage:

    def __init__(self, m: int, k: int):
        self.element = []
        self.m, self.k = m, k

    def addElement(self, num: int) -> None:
        self.element.append(num)

    def calculateMKAverage(self) -> int:
        # print(self.element)
        if len(self.element) < self.m:
            return -1
        content = self.element[-self.m:]
        # print(content)
        content.sort()
        a = sum(content[self.k:-self.k])
        b = len(content) - 2 * self.k
        ans = a // b + 1 if (a / b - a // b) > 0.5 else a // b
        return ans


# Your MKAverage object will be instantiated and called as such:

# ["MKAverage","addElement","addElement","calculateMKAverage","addElement","calculateMKAverage","addElement","addElement","addElement","calculateMKAverage"]
# [[3,1],[3],[1],[],[10],[],[5],[5],[5],[]]
if __name__ == '__main__':
    m, k = 3, 1
    obj = MKAverage(m, k)
    obj.addElement(3)
    obj.addElement(1)
    print(obj.calculateMKAverage())
    obj.addElement(10)
    print(obj.calculateMKAverage())
    obj.addElement(5)
    obj.addElement(5)
    obj.addElement(5)
    print(obj.calculateMKAverage())
