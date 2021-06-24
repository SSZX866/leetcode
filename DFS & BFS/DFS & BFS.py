# -*- coding: utf-8 -*-
# @Time    : 2021/6/21 16:29
# @File    : DFS AND BFS.py
from leetcode import *


# BFS
def bfs_Model(target):
    N = len(target)
    for i in range(N):
        # 如果满足条件
        if target[i]:
            que = deque([target[i]])
            target[i] = False
            while que:
                tmp = que.popleft()  # 弹出队首元素
                for each in tmp.neibor:  # 每一个相邻满足条件的元素加入队列
                    if target[each]:
                        que.append(each)
                        target[each] = False


# DFS
def dfs_Model(target):
    def dfs(thisTarget, index):
        for each in thisTarget[index].neibor:
            if not thisTarget[each]:
                continue
            thisTarget[each] = False
            dfs(thisTarget, each)

    N = len(target)
    for i in range(N):
        if not target[i]:
            continue
        target[i] = False
        dfs(target, i)


# DFS with stack 只需要把 BFS的队列换成栈即可
def bfs_Model(target):
    N = len(target)
    for i in range(N):
        # 如果满足条件
        if target[i]:
            stack = [target[i]]
            target[i] = False
            while stack:
                tmp = stack.pop()  # 弹出栈内元素
                for each in tmp.neibor:  # 每一个相邻满足条件的元素加入队列
                    if target[each]:
                        stack.append(each)
                        target[each] = False
