# -*- coding: utf-8 -*-
# @Time    : 2021/07/26 11:42
# @File    : 1947. 最大兼容性评分和
from leetcode import *


class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        n = len(students)
        m = len(students[0])
        tmp = []
        for i in range(n):
            for j in range(n):
                tmp.append((i, j))
        ans = 0
        print(tmp)
        for i, j in tmp:
            cnt = 0
            for idx in range(m):
                if students[i][idx] == mentors[j][idx]:
                    cnt += 1
            ans = max(ans, cnt)
        return ans


if __name__ == '__main__':
    students = [[1, 1, 0], [1, 0, 1], [0, 0, 1]]
    mentors = [[1, 0, 0], [0, 0, 1], [1, 1, 0]]
    print(Solution().maxCompatibilitySum(students, mentors))
