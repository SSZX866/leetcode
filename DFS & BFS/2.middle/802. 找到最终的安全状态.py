# -*- coding: utf-8 -*-
# @Time    : 2021/08/05 11:20
# @File    : 802. 找到最终的安全状态
from leetcode import *


# 本题安全的定义可以看作是反向图的拓扑排序
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        reverse_graph = defaultdict(list)
        Indegree = [0] * len(graph)
        # 构建反图，统计图的入度（就是反图的出度）
        for i, start in enumerate(graph):
            for end in start:
                reverse_graph[end].append(i)
                Indegree[i] += 1
        # 在反图上进行拓扑排序
        que = deque()
        for i in range(len(Indegree)):
            if Indegree[i] == 0:
                que.append(i)
        while que:
            cur = que.popleft()
            for each in reverse_graph[cur]:
                Indegree[each] -= 1
                if Indegree[each] == 0:
                    que.append(each)
        return [i for i in range(len(Indegree)) if Indegree[i] == 0]

