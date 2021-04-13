# -*- coding: utf-8 -*-
# @Time    : 2021/4/11 10:59
# @File    : 5728. 最少侧跳次数.py
from typing import List


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        run, ans, flag = 2, 0, [False, 0]  # flag延后选择赛道
        for i in range(len(obstacles)):
            if obstacles[i] == run and not flag[0]:
                if obstacles[i - 1] != 0:
                    run = 6 - obstacles[i - 1] - run
                else:
                    flag = [True, obstacles[i]]
                ans += 1
            elif flag[0]:
                if obstacles[i] != flag[1] and obstacles[i] != 0:
                    run = 6 - flag[1] - obstacles[i]
                    flag = [False, 0]
            # print(run, flag,ans)
        return ans

if __name__ == '__main__':
    obstacles = [0, 1, 2, 3, 0]
    obstacles = [0, 1, 1, 3, 3, 0]
    obstacles = [0, 2, 1, 0, 3, 0]
    obstacles = [0, 2, 2, 1, 0, 3, 0, 3, 0, 1, 0]
    print(Solution().minSideJumps(obstacles))