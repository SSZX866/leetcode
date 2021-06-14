# -*- coding: utf-8 -*-
# @Time    : 2021/6/13 10:52
# @File    : 5785. 合并若干三元组以形成目标三元组.py
from leetcode import *


# 贪心模拟，失败
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        tmp = [[i, target[i]] for i in range(len(target))]
        tmp.sort(key=lambda x: x[1], reverse=True)
        mark = False
        pre = 1001
        for i in range(len(triplets)):
            if triplets[i][tmp[0][0]] == tmp[0][1] and triplets[i][tmp[1][0]] <= tmp[1][1] and triplets[i][tmp[2][0]] <= \
                    tmp[2][1]:
                if not mark:
                    index = i
                mark = True
                tmp1 = min(pre, triplets[i][tmp[1][0]])
                if pre == tmp1:
                    index = i
                pre = tmp1
        if not mark: return False
        mark = False
        print(tmp)
        print(pre, tmp[1][0])
        pre1 = 1001
        for i in range(len(triplets)):
            if triplets[i][tmp[1][0]] == tmp[1][1] and triplets[i][tmp[1][0]] >= pre and triplets[i][tmp[2][0]] <= \
                    tmp[2][1] and triplets[i][tmp[1][0]] <= tmp[1][1] and triplets[index][tmp[0][0]] <= triplets[i][
                tmp[0][0]]:
                if not mark:
                    nextindex = i
                mark = True
                print(triplets[i][tmp[2][0]])
                tmp1 = min(pre1, triplets[i][tmp[2][0]])
                if pre == tmp1:
                    nextindex = i
                pre1 = tmp1
        if not mark: return False
        print(pre1, tmp[2][0])
        for i in range(len(triplets)):
            print(triplets[i][tmp[2][0]], tmp[2][1], triplets[i][tmp[2][0]], pre1, triplets[i][tmp[2][0]] == tmp[2][1],
                  triplets[i][tmp[2][0]] >= pre1)
            if triplets[i][tmp[2][0]] == tmp[2][1] and triplets[i][tmp[2][0]] >= pre1 and triplets[index][tmp[0][0]] <= \
                    triplets[i][tmp[0][0]] and triplets[nextindex][tmp[1][0]] <= triplets[i][tmp[1][0]]:
                return True
        return False


# 脑筋急转弯，去掉所有大于等于目标对应值的数组，在剩下的数组中寻找是否存在目标数组的值，若都存在则True
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        tmp = []
        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                tmp.append(triplet)
        tmp = list(zip(*tmp))
        if not tmp: return False
        for i in range(3):
            if target[i] not in tmp[i]:
                return False
        return True


if __name__ == '__main__':
    triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
    target = [2, 7, 5]
    triplets = [[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]]
    target = [5, 5, 5]
    triplets = [[1, 3, 4], [2, 5, 8]]
    target = [2, 5, 8]
    triplets = [[3, 4, 5], [4, 5, 6]]
    target = [3, 2, 5]
    triplets = [[3, 5, 1], [10, 5, 7]]
    target = [3, 5, 7]
    triplets = [[3, 1, 7], [1, 5, 10]]
    target = [3, 5, 7]
    print(Solution().mergeTriplets(triplets, target))
