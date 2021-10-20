# -*- coding: utf-8 -*-
# @Time    : 2021/10/19 15:41
# @File    : 211. 添加与搜索单词 - 数据结构设计.py
from leetcode import *

DICT = {chr(ord('a') + i): i for i in range(26)}


class WordDictionary:
    def __init__(self):
        self.dic = [[[set() for _ in range(26)] for _ in range(i)] for i in range(501)]

    def addWord(self, word: str) -> None:
        i = len(word)
        for j in range(i):
            self.dic[i][j][DICT[word[j]]].add(word)

    def search(self, word: str) -> bool:
        res = []
        i = len(word)
        for index in range(i):
            if word[index] != '.':
                res.append((index, word[index]))
        s = None
        for j, c in res:
            if s == None:
                s = self.dic[i][j][DICT[c]]
            else:
                s &= self.dic[i][j][DICT[c]]
            if len(s) == 0: return False
        return True


# 用例11耗时太久
class WordDictionary:
    def __init__(self):
        self.len_dic = dict()
        self.dic = []  # dic[i][j][k] 长度为n第j个字母为k的集合 其中i=len_dic(n)
        self.index = 0

    def addWord(self, word: str) -> None:
        # unsharable
        n = len(word)
        if n not in self.len_dic:
            self.dic.append([[set() for _ in range(26)] for _ in range(n)])
            self.len_dic[n] = self.index
            self.index += 1
        i = self.len_dic[n]
        for j in range(n):
            self.dic[i][j][DICT[word[j]]].add(word)

    def search(self, word: str) -> bool:
        res = []
        n = len(word)
        if n not in self.len_dic: return False
        i = self.len_dic[n]
        for index in range(n):
            if word[index] != '.':
                res.append((index, word[index]))
        s = None
        for j, c in res:
            if s is None:
                # 直接赋值在下面取交集会修改原集合！！！
                # s = self.dic[i][j][DICT[c]]
                # s = copy.deepcopy(self.dic[i][j][DICT[c]])
                s = set(self.dic[i][j][DICT[c]])
            else:
                s &= self.dic[i][j][DICT[c]]
            if len(s) == 0: return False
        return True


# 字典树
class WordDictionary:

    def __init__(self):
        self.trie = dict()

    def addWord(self, word: str) -> None:
        cur = self.trie
        for c in word:
            if c in cur:
                cur = cur[c]
            else:
                cur[c] = {}
                cur = cur[c]
        cur["#"] = {}

    def search(self, word: str) -> bool:
        word += "#"
        bfs = deque([(0, self.trie)])
        while bfs:
            idx, cur = bfs.popleft()
            if idx == len(word):
                return True
            if word[idx] == '.':
                for nxt in cur.values():
                    bfs.append((idx + 1, nxt))
            elif word[idx] in cur:
                bfs.append((idx + 1, cur[word[idx]]))
        return False


if __name__ == '__main__':
    funcs = ["addWord", "addWord", "addWord", "search", "search", "search", "search", "addWord", "search"]
    value = [["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."], ["afds"], ["...s"]]
    obj = WordDictionary()
    ans = []
    for i in range(len(funcs)):
        try:
            ans.append(eval("obj." + funcs[i] + "('" + value[i][0] + "')"))
        except:
            print("obj." + funcs[i] + "(" + value[i][0] + ")")

    # print(ans)