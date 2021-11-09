# -*- coding: utf-8 -*-
# @Time    : 2021/11/9 08:59
# @File    : 488. 祖玛游戏.py
from leetcode import *


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        @functools.lru_cache(None)
        def dfs(cur, handLeft):
            # print(cur, handLeft)
            if not cur: return len(hand) - len(handLeft)
            if not handLeft: return -1
            ans = 6
            for j in range(len(cur) + 1):
                for k in range(len(handLeft)):
                    t = cur[:j] + handLeft[k] + cur[j:]
                    h = handLeft[:k] + handLeft[k + 1:]
                    while "RRR" in t or "YYY" in t or "BBB" in t or "GGG" in t or "WWW" in t:
                        s = ""
                        prev, cnt = t[0], 1
                        for i in range(1, len(t)):
                            if t[i] == prev:
                                cnt += 1
                            else:
                                if cnt < 3: s += prev * cnt
                                prev = t[i]
                                cnt = 1
                        if cnt < 3: s += prev * cnt
                        t = s
                    tmp = dfs(t, h)
                    if tmp != -1: ans = min(tmp, ans)
            return ans if ans != 6 else -1

        return dfs(board, hand)


if __name__ == '__main__':
    board = "WRRBBW"
    hand = "RB"
    board = "WWRRBBWW"
    hand = "WRBRW"
    board = "RBYYBBRRB"
    hand = "YRBGB"
    board = "WR"
    hand = "WWRR"
    print(Solution().findMinStep(board, hand))
