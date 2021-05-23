# -*- coding: utf-8 -*-
# @Time    : 2021/5/23 12:47
# @File    : 1707. 与数组中元素的最大异或值.py
from leetcode import *


class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left  # 1
        self.right = right  # 0

# 超时！！！
class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        dic = defaultdict(list)
        for i in range(len(queries)):
            dic[str(queries[i])].append(i)
        queries.sort(key=lambda x: x[1])
        root = Tree(0)
        ans = []
        pre = 0
        MAX = len(bin(max(nums))) - 1
        for query in queries:
            if nums[0] > query[1]:
                ans.append(-1)
            else:
                index = bisect.bisect_left(nums, query[1])
                ans.append(
                    self.findMaximumXOR(
                        nums[pre:index] if index < len(nums) and nums[index] != query[1] else nums[pre:index + 1],
                        query[0], root, MAX))
                pre = index if index < len(nums) and nums[index] != query[1] else index + 1
        tmp = [0] * len(queries)
        for i in range(len(queries)):
            for index in dic[str(queries[i])]:
                tmp[index] = ans[i]
        return tmp

    def findMaximumXOR(self, nums, target, root, MAX):
        for num in nums:
            b = bin(num)[2:]
            b = (MAX - len(b)) * '0' + b
            node = root
            for byte in b:
                if byte == '1':
                    if not node.left:
                        node.left = Tree(1)
                    node = node.left
                else:
                    if not node.right:
                        node.right = Tree(0)
                    node = node.right
        b = bin(target)[2:]
        b = (MAX - len(b)) * '0' + b
        node, tmp = root, ''
        for byte in b:
            if byte == '1':
                if node.right:
                    tmp += '1'
                    node = node.right
                else:
                    tmp += '0'
                    node = node.left
            else:
                if node.left:
                    tmp += '1'
                    node = node.left
                else:
                    tmp += '0'
                    node = node.right
        return int(tmp, 2)


if __name__ == '__main__':
    nums = [0, 1, 2, 3, 4]
    queries = [[3, 1], [1, 3], [5, 6]]
    nums = [62992, 597298, 425096846, 848555587, 654414084]
    queries = [[837555559, 282304038], [315703954, 1000000000], [10515140, 264595091], [631966635, 1000000000],
               [158538211, 1000000000]]
    print(Solution().maximizeXor(nums, queries))
