# -*- coding: utf-8 -*-
# @Time    : 2021/8/21 10:15
# @File    : demo.py
import copy

from leetcode import *


def demo():
    white, black = 0, 0
    need = []
    n = input()
    while n:
        tmp = input()
        if tmp == 1: white += 1
        if tmp == 2: black += 1
        if tmp == 0:
            need.append([])
            need[-1].append(input())
            need[-1].append(input())
        n -= 1
    if black > white:
        delta = black - white
        if len(need) < delta or delta % 2 != len(need) % 2:
            return -1


def demo1():
    n = int(input())
    target = 0
    graph = []
    for i in range(n):
        graph.append([])
        for each in input().split():
            graph[-1].append(each)
            if graph[-1][-1] == '.':
                target += 1
    print(graph)
    # graph = [['.', '.', '#'], ['.', '.', '#'], ['.', '.', '.']]
    # n = 3
    if graph[0][0] == '#': return 0
    visit = {(0, 0)}

    def dfs(x, y):
        ans = 0
        if len(visit) == target:
            return 1
        for x_, y_ in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            tmpx = x + x_
            tmpy = y + y_
            if not (0 <= tmpx < n and 0 <= tmpy < n) or (tmpx, tmpy) in visit or graph[tmpx][tmpy] == '#':
                continue
            visit.add((tmpx, tmpy))
            ans += dfs(tmpx, tmpy)
            visit.remove((tmpx, tmpy))
        return ans

    return dfs(0, 0)


class Solution:
    dp = [None] * 27
    dp[1] = 'a'

    def invert(self, s):
        tmp = ''
        for c in s:
            tmp += chr(25 - ord(c) + 2 * ord('a'))
        return tmp

    def func(self, n, k):
        if self.dp[n] is not None:
            return self.dp[n]
        self.dp[n] = self.func(n - 1, k) + chr(ord('a') + (n - 1)) + self.invert(self.func(n - 1, k))[::-1]
        return self.dp[n]

    def findKthBit(self, n, k):
        return self.func(n, k)[k - 1]


# print(Solution().findKthBit(24,11))

class Solution:
    def minSai(self, graph):
        n, m = len(graph), len(graph[0])
        visit = {(0, 0)}
        if graph[-1][-1] == 2 or graph[0][0] == 2: return -1
        ans = None
        cost = 0

        def dfs(x, y):
            nonlocal ans, cost
            if x == n - 1 and y == m - 1:
                if ans is None:
                    ans = cost
                else:
                    ans = min(ans, cost)

                return
            for x_, y_ in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                tmpx = x + x_
                tmpy = y + y_
                if not (0 <= tmpx < n and 0 <= tmpy < m) or (tmpx, tmpy) in visit or graph[tmpx][tmpy] == 2:
                    continue
                visit.add((tmpx, tmpy))
                cost += 1 if graph[tmpx][tmpy] == 1 else 2
                dfs(tmpx, tmpy)
                cost -= 1 if graph[tmpx][tmpy] == 1 else 2
                visit.remove((tmpx, tmpy))
            return

        dfs(0, 0)
        return ans


graph = [[1, 1, 1, 1, 0],
         [0, 1, 0, 1, 0],
         [1, 1, 2, 1, 1],
         [0, 2, 0, 0, 1]]
print(Solution().minSai(graph))
