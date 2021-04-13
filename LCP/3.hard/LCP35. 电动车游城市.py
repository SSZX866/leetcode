# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 15:42
# @File    : 3. 电动车游城市.py
from typing import List


class Solution:
    def electricCarPlan(self, paths: List[List[int]], cnt: int, start: int, end: int, charge: List[int]) -> int:
        res = [10000000]

        def backtrace(paths, path, res, end, cur):
            if path and cur == end:
                tmp = (charge[start] + 1) * path[0][2]
                for i in range(len(path) - 1):
                    tmp += (charge[path[i][3]] + 1) * path[i + 1][2]
                res[:] = [min(res[0], tmp)]
                print(path, res)
                return
            for p in paths:
                if path:
                    cur = p[0] if path[-1][-1] == p[1] else p[1]
                if not path and start in p[:2]:
                    cur = p[0] if start == p[1] else p[1]
                    if cur != start:
                        path.append(p + [cur])
                        backtrace(paths, path, res, end, cur)
                        path.pop()
                elif path and p[2] <= cnt and cur not in [node[3] for node in path] and path[-1][-1] in p[
                                                                                                        :2] and cur != start:
                    path.append(p + [cur])
                    backtrace(paths, path, res, end, cur)
                    path.pop()

        # for p in paths:
        #     if start in p[:2]:
        #         if p[0] == start:
        #             backtrace(paths,[p+[start]],res,end,start)

        backtrace(paths, [], res, end, start)
        return res[0]


if __name__ == '__main__':
    # print(Solution().electricCarPlan(paths=[[1, 3, 3], [3, 2, 1], [2, 1, 3], [0, 1, 4], [3, 0, 5]], cnt=6, start=1, end=0,charge=[2, 10, 4, 1]))
    print(Solution().electricCarPlan(paths = [[0,4,2],[4,3,5],[3,0,5],[0,1,5],[3,2,4],[1,2,8]], cnt = 8, start = 0, end = 2, charge = [4,1,1,3,2]))
