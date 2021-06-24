# -*- coding: utf-8 -*-
# @Time    : 2021/6/24 20:33
# @File    : 210. 课程表 II.py
from leetcode import *


# DFS
# 思路：同207一样判断是否有环，在初次访问节点（即访问状态为0）时将临时列表反转，在回溯时将节点添加临时列表中，
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for end, start in prerequisites:
            graph[start].append(end)
        ans = []

        def dfs(u):

            if visited[u] == 1: return True
            if visited[u] == 2: return False
            visited[u] = 2
            reversed(tmp)
            for v in graph[u]:
                if not dfs(v): return False
            visited[u] = 1
            tmp.append(u)
            return True

        for i in range(numCourses):
            tmp = []
            if not dfs(i): return []
            ans.extend(tmp)
        return ans[::-1]


# 官方DFS
# 只需要在回溯是入栈即可，不需要临时列表
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for end, start in prerequisites:
            graph[start].append(end)
        ans = []

        def dfs(u):

            if visited[u] == 1: return True
            if visited[u] == 2: return False
            visited[u] = 2
            for v in graph[u]:
                if not dfs(v): return False
            visited[u] = 1
            ans.append(u)
            return True

        for i in range(numCourses):
            if not dfs(i): return []
        return ans[::-1]


# BFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for end, start in prerequisites:
            graph[start].append(end)
            indegree[end] += 1
        que = deque()
        visited = 0
        ans = []
        for i in range(numCourses):
            if indegree[i] == 0:
                que.append(i)
        while que:
            cur = que.popleft()
            visited += 1
            ans.append(cur)
            for each in graph[cur]:
                indegree[each] -= 1
                if indegree[each] == 0:
                    que.append(each)
        return ans if visited == numCourses else []


if __name__ == '__main__':
    print(Solution().findOrder(2, [[1, 0]]))
    print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
