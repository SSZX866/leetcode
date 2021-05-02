# -*- coding: utf-8 -*-
# @Time    : 2021/5/2 00:21
# @File    : 554. 砖墙.py
from collections import Counter

from leetcode import *


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        pre, end, length = [0], sum(wall[0]), len(wall)
        for layer in wall:
            pre.append(0)
            for each in layer:
                pre.append(each + pre[-1])
        ans = Counter(pre)
        del ans[0]  # 去掉开头缝隙
        del ans[end]  # 去掉结尾缝隙
        # print(ans,ans.most_common()[0][1])
        # return len(wall) - ans[max(ans, key=lambda x: ans[x])] if ans else len(wall)
        return length - ans.most_common()[0][1] if ans else length


if __name__ == '__main__':
    wall = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]
    wall = [[1], [1], [1]]
    wall = [[1, 1], [2], [1, 1]]
    print(Solution().leastBricks(wall))
