# -*- coding: utf-8 -*-
# @Time    : 2021/8/24 14:25
# @File    : 797. 所有可能的路径.py
from leetcode import *


# dfs
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(list)
        for i in range(len(graph)):
            dic[i].extend(graph[i])
        n = len(graph)
        ans = []

        def dfs(cur, path):
            if cur == n - 1:
                ans.append(path[:])
            for each in dic[cur]:
                path.append(each)
                dfs(each, path)
                path.pop()

        dfs(0, [0])
        return ans


# bfs
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(list)
        for i, ends in enumerate(graph):
            dic[i].extend(ends)
        n, queue, ans = len(graph), deque([[0]]), []
        while queue:
            path = queue.popleft()
            for point in dic[path[-1]]:
                newPath = path + [point]
                if point == n - 1:
                    ans.append(newPath)
                else:
                    queue.append(newPath)
        return ans
