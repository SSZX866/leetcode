# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 22:52
# @File    : 5733. 最近的房间.py
from leetcode import *


class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        rooms.sort(key=lambda x: (x[1], x[0]))
        # rooms = sorted([room + [i] for i, room in enumerate(rooms)], key=lambda x: (x[1], x[0]))
        # queries.sort(key=lambda x: (x[1], x[0]))
        queries = sorted([querie + [i] for i, querie in enumerate(queries)], key=lambda x: (x[1], x[0]))
        print(rooms,queries)
        i, j, n, m, tmp, pre = 0, 0, len(rooms), len(queries), [], float('inf')
        while i < n and j < m:
            if rooms[i][1] >= queries[j][1]:
                distance = abs(rooms[i][0] - queries[j][0])
                if distance < pre and i != n - 1:
                    pre = distance
                    i += 1
                    print(distance, pre, i, j)
                    continue
                if i == n - 1:
                    tmp.append([rooms[i][0], queries[j][2]])
                else:
                    tmp.append([rooms[i - 1][0], queries[j][2]])
                j += 1
            else:
                i += 1
        ans = [-1 for _ in range(m)]
        print(tmp)
        for t in tmp:
            ans[t[1]] = t[0]
        return ans


if __name__ == '__main__':
    rooms = [[2, 2], [1, 2], [3, 2]]
    queries = [[3, 1], [3, 3], [5, 2]]
    rooms = [[1, 4], [2, 3], [3, 5], [4, 1], [5, 2]]
    queries = [[2, 3], [2, 4], [2, 5]]
    print(Solution().closestRoom(rooms, queries))
