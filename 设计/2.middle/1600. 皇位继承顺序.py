# -*- coding: utf-8 -*-
# @Time    : 2021/6/20 20:25
# @File    : 1600. 皇位继承顺序.py
from leetcode import *


class KingTree:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = KingTree(kingName, [])
        self.deathList = set()
        self.familyList = {kingName: self.root}

    def birth(self, parentName: str, childName: str) -> None:
        # que = deque([self.root])
        # while que:
        #     tmp = que.popleft()
        #     if tmp.val == parentName:
        #         tmp.children.append(KingTree(childName, []))
        #         break
        #     for child in tmp.children:
        #         que.append(child)
        childTree = KingTree(childName, [])
        self.familyList[parentName].children.append(childTree)
        self.familyList[childName] = childTree

    def death(self, name: str) -> None:
        self.deathList.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ans = []
        stack = [self.root]
        while stack:
            tmp = stack.pop()
            if tmp.val not in self.deathList:
                ans.append(tmp.val)
            for child in tmp.children[::-1]:
                stack.append(child)
        return ans


if __name__ == '__main__':
    test = ThroneInheritance("king")
    test.birth("king", "andy")
    test.birth("king", "bob")
    test.birth("king", "catherine")
    test.birth("andy", "matthew")
    test.birth("bob", "alex")
    test.birth("bob", "asha")
    print(test.getInheritanceOrder())
    test.death("bob")
    print(test.getInheritanceOrder())
