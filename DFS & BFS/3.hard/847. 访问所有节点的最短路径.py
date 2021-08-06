# -*- coding: utf-8 -*-
# @Time    : 2021/08/06 10:51
# @File    : 847. 访问所有节点的最短路径
from leetcode import *
# BFS + 状态压缩
# 用一个长度为n的二进制表示每个点被走过的状态(该位为0表示没走过，该位为1表示走过)
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # 初始以每个点为起点
        queue = deque([(i, 1 << i) for i in range(len(graph))])
        visit = set(queue)
        step = 0
        # 目标为2^n - 1
        target = (1 << len(graph)) - 1
        while queue:
            cur_que = queue
            queue = deque()
            while cur_que:
                node, state = cur_que.popleft()
                if state == target: return step
                for nx in graph[node]:
                    successor = (nx, 1 << nx | state)
                    if successor not in visit:
                        visit.add(successor)
                        queue.append(successor)
            step += 1
        return -1
