# -*- coding: utf-8 -*-
# @Time    : 2021/6/28 18:34
# @File    : 815. 公交路线.py
from leetcode import *


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if target == source: return 0
        N = len(routes)
        dic = defaultdict(list)
        for i in range(N):
            for each in routes[i]:
                dic[each].append(i)

        def getStatus(status):
            statusList = []
            for each in routes[status]:
                statusList.extend(dic[each])
            return statusList

        def bfs(index):
            visited = {index}
            que = deque([index])
            step = 1
            while que:
                step += 1
                curQue = que
                que = deque()
                while curQue:
                    tmp = curQue.popleft()
                    for each in getStatus(tmp):
                        if each in visited:
                            continue
                        visited.add(each)
                        if target in routes[each]:
                            return step
                        que.append(each)
            return -1

        ans = 501
        for i in range(N):
            if source in routes[i]:
                if target in routes[i]: return 1
                thisStep = bfs(i)
                if thisStep != -1: ans = min(bfs(i), ans)
        return ans if ans != 501 else -1


if __name__ == '__main__':
    routes = [[2], [2, 8]]
    source = 8
    target = 2
    print(Solution().numBusesToDestination(routes, source, target))
