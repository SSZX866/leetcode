# -*- coding: utf-8 -*-
# @Time    : 2021/3/23 9:51
# @File    : 341. 扁平化嵌套列表迭代器.py
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """
import re
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.list = re.findall('-?\d+', str(nestedList))
        # self.list = str(nestedList).replace('[', '').replace(']', '').split(', ')

    def next(self) -> int:
        return int(self.list.pop(0))

    def hasNext(self) -> bool:
        return self.list != []
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
if __name__ == '__main__':
    i, v = NestedIterator([[1,1],2,[1,1]]), []
    while i.hasNext(): v.append(i.next())
    print(v)