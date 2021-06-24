# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 13:19
# @File    : 207. 课程表.py
# 本题本质是判断有向图是否有环，通常采用DFS或BFS方法
from leetcode import *


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites or not prerequisites[0]: return True
        courseList = []
        for prerequisite in prerequisites:
            mark = False
            for i in range(len(courseList)):
                if prerequisite[0] in courseList[i]:
                    if prerequisite[1] in courseList[i]:
                        return False
                    courseList[i].add(prerequisite[1])
                    mark = True
            if not mark:
                if prerequisite[0] == prerequisite[1]: return False
                courseList.append({prerequisite[0], prerequisite[1]})
        return True


# DFS 一条路走到底
# 当且仅当遇见已访问过这条 支 路 中的节点时判断为有环，
# 注意，“遇到了任何在这条支路中已经访问过的节点”和“遇到了任何已经访问过的节点”，是不同的概念。
# 因此需要标记三种状态
# 0：未访问过 2：在这条支路中已访问过 1：已经访问过的节点
# 在某条DFS的路径上，第一次遇到的节点i的时候标记2.在回溯返回节点i的时候标记1
# 因为能成功返回的话，说明后续的节点都没有环，都是死胡同，此后任何任何入度指向这个节点i的话，我们都不用担心后续的遍历会遇到环
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses
        for end, start in prerequisites:
            graph[start].append(end)

        def dfs(u):
            if visited[u] == 1:
                return True
            if visited[u] == 2:
                return False
            # 进入支路时标记为2
            visited[u] = 2
            for v in graph[u]:
                if not dfs(v): return False
            # 回溯时标记为1
            visited[u] = 1
            return True

        for i in range(numCourses):
            if not dfs(i): return False
        return True


# BFS 拓扑排序的思想，循环去掉所有入度为0的节点，如果最后还有剩余，那么一定为环
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        Indegree = [0 for _ in range(numCourses)]  # 保存入度
        # 生成图，记录入度
        for end, start in prerequisites:
            graph[start].append(end)
            Indegree[end] += 1

        # 将入度为0的节点放入队列（栈也可以，顺序不影响结果,但不是标准的BFS）
        que = deque()
        for i in range(numCourses):
            if Indegree[i] == 0:
                que.append(i)

        # visited = 0
        while que:
            cur = que.popleft()
            # visited += 1
            # 修改所有与该节点所指向节点的入度
            for each in graph[cur]:
                Indegree[each] -= 1
                if Indegree[each] == 0:
                    que.append(each)
        # 如果所有节点中，仍然存在入度不为0的节点即存在环
        # 或者可以记录所有遍历的节点数是否等于总节点数
        for each in Indegree:
            if each != 0:
                return False
        return True
        # return visited == numCourses


if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0]]
    prerequisites = [[1, 0], [0, 1]]
    numCourses = 20
    prerequisites = [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]
    numCourses = 3
    prerequisites = [[0, 1], [0, 2], [1, 2]]
    prerequisites = [[1, 1]]
    print(Solution().canFinish(numCourses, prerequisites))
