# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 10:37
# @File    : 5801. 消灭怪物的最大数量.py
from leetcode import *


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        lo, hi = 1, len(dist)
        n = len(dist)
        tmp = []
        for i in range(n):
            tmp.append(math.ceil(dist[i] / speed[i]))
        # tmp.sort()
        counter = Counter(tmp)

        ans = 0
        i = 0
        print(counter)
        keys = sorted(counter.keys())
        for t in range(n):
            print(i,counter[keys[i]],t)
            if i < len(keys) and counter[keys[i]] > 0 and keys[i] - t > 0:
                ans += 1
                counter[keys[i]] -= 1
                if counter[keys[i]] == 0:
                    i += 1
            else:
                break

        print(counter)
        return ans
        # def check(target):
        #     cnt = 0
        #     for i in range(n):
        #         if math.ceil(dist[i] / speed[i]) >= target:
        #             cnt += 1
        #         if cnt >= target:
        #             return False
        #     return True
        #
        # while lo < hi:
        #     mid = lo + (hi - lo) // 2
        #     if check(mid):
        #         lo = mid + 1
        #     else:
        #         hi = mid
        # return lo


if __name__ == '__main__':
    # dist = [1, 3, 4]
    # speed = [1, 1, 1]
    dist = [1, 1, 2, 3]
    speed = [1, 1, 1, 1]
    dist = [3, 2, 4]
    speed = [5, 3, 2]
    dist = [4, 2, 3]
    speed = [2, 1, 1]
    # dist = [4, 2, 8]
    # speed = [2, 1, 4]
    dist = [4, 3, 3, 3, 4]
    speed = [1, 1, 1, 1, 4]
    print(Solution().eliminateMaximum(dist, speed))
