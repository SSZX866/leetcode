# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 00:03
# @File    : 690. 员工的重要性.py
from leetcode import *


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employees.sort(key=lambda x: x.id)
        dic, ans = set(), []
        for employee in employees:
            if employee.id in dic or employee.id == id:
                ans.append(employee.importance)
                for i in employee.subordinates: dic.add(i)
        return sum(ans)


if __name__ == '__main__':
    employees = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
    id = 1
    print(Solution().getImportance(employees, id))
