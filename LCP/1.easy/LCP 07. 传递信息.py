# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 12:54
# @File    : LCP 07. 传递信息.py
from leetcode import *


# bfs
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        dic = defaultdict(list)
        for each in relation:
            dic[each[0]].append(each[1])
        queue = deque([0])
        ans = 0
        while queue:
            k -= 1
            curQueue = queue
            queue = deque()
            while curQueue:
                tmp = curQueue.popleft()
                for each in dic[tmp]:
                    if not k and each == n - 1:
                        ans += 1
                    queue.append(each)
            if not k:
                return ans


# dfs recursion
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        dic = defaultdict(list)
        for each in relation:
            dic[each[0]].append(each[1])
        ans = 0

        def dfs(index, depth):
            nonlocal ans
            if depth == k:
                if index == n - 1:
                    ans += 1
                return
            for each in dic[index]:
                dfs(each, depth + 1)

        dfs(0, 0)
        return ans


# dfs stack
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        dic = defaultdict(list)
        for each in relation:
            dic[each[0]].append(each[1])
        ans = 0

        stack = [[0, 0]]  # [index,depth]
        while stack:
            index, depth = stack.pop()
            if depth == k:
                if index == n - 1:
                    ans += 1
                continue
            for each in dic[index]:
                stack.append([each, depth + 1])
        return ans


# dp
# dp[i][each[1]] += dp[i - 1][each[0]] i:depth,j:index 深度为i层时玩家j到达的数量
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        dp = [[0] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 1
        for i in range(1, k + 1):
            for each in relation:
                dp[i][each[1]] += dp[i - 1][each[0]]
        return dp[k][n - 1]


if __name__ == '__main__':
    n = 5
    relation = [[0, 2], [2, 1], [3, 4], [2, 3], [1, 4], [2, 0], [0, 4]]
    k = 3
    print(Solution().numWays(n, relation, k))
