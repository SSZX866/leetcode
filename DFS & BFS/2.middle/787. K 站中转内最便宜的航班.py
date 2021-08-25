# -*- coding: utf-8 -*-
# @Time    : 2021/8/24 12:47
# @File    : 787. K 站中转内最便宜的航班.py
from leetcode import *


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dic = defaultdict(list)
        for start, end, price in flights:
            dic[start].append((end, price))
        queue = deque([(src, 0, {src})])
        step = 0
        ans = None
        while queue:
            cur = queue
            queue = deque()
            step += 1
            while cur:
                node, curPrice, visited = cur.popleft()
                for nextPoint, cost in dic[node]:
                    if nextPoint in visited:
                        continue
                    newVisited = visited & {nextPoint}
                    newCost = curPrice + cost
                    if nextPoint == dst:
                        if not ans:
                            ans = newCost
                        else:
                            ans = min(ans, newCost)
                        continue
                    queue.append((nextPoint, newCost, newVisited))
            if step > k: break
        return ans if ans is not None else -1


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        inf = 1 << 32
        connect = defaultdict(dict)
        for a, b, c in flights:
            connect[a][b] = c

        @lru_cache(None)
        def dfs(city, remain):
            if city == dst:
                return 0
            if not remain:
                return inf
            remain -= 1
            ans = inf
            for nxt in connect[city]:
                ans = min(ans, dfs(nxt, remain) + connect[city][nxt])
            return ans

        res = dfs(src, k + 1)
        return res if res != inf else -1
