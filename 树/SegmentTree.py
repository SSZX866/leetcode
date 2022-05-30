# -*- coding: utf-8 -*-
# @Time    : 2022/05/30 14:07
# @File    : SegmentTree
class SegmentTree:
    def __init__(self, nums):
        # 下标从1开始
        self.nums = [0] + nums
        self.n = n = len(self.nums)
        self.tr = [0] * 4 * n
        self._build(1, 1, n - 1)

    # 更新nums[index] = val
    def update(self, index, val):
        # 增加增量， 线段树数组从1开始，所以index+1
        self._add(1, 1, self.n - 1, index + 1, val - self.nums[index + 1])
        self.nums[index + 1] = val

    # 查询区间[left, right]和
    def query(self, left, right):
        return self._calc(1, 1, self.n - 1, left + 1, right + 1)

    # 建树
    # i为区间l到r的和在线段树中的下标， 即self.tr[i] = sum(nums[l:r + 1])
    # i的左儿子为i*2 即 i << 1, 右儿子为 i * 2 + 1即i << 1 | 1
    def _build(self, i, l, r):
        if l == r:
            self.tr[i] = self.nums[l]
            return
        m = (l + r) >> 1
        # self._build(i + i, l, m)
        self._build(i << 1, l, m)
        # self._build(i + i + 1, m + 1, r)
        self._build(i << 1 | 1, m + 1, r)
        # self.tr[i] = self.tr[i + i] + self.tr[i + i + 1]
        self.tr[i] = self.tr[i << 1] + self.tr[i << 1 | 1]

    # 单点修改
    # 将nums[x] + y，更新线段树，其中 l <= x <= r
    def _add(self, i, l, r, x, y):
        self.tr[i] += y
        if l == r:
            return
        m = (l + r) >> 1
        if x <= m:
            self._add(i << 1, l, m, x, y)
        else:
            self._add(i << 1 | 1, m + 1, r, x, y)

    # 求sum(nums[s:t+1]), 其中[s:t+1]包含于[l:r+1]中
    def _calc(self, i, l, r, s, t):
        # 区间恰好重叠
        if l == s and r == t:
            return self.tr[i]
        # l <= s <= t <= r 根据m落在不同的位置递归计算
        m = (l + r) >> 1
        if t <= m:
            return self._calc(i << 1, l, m, s, t)
        elif s > m:
            return self._calc(i << 1 | 1, m + 1, r, s, t)
        else:
            return self._calc(i << 1, l, m, s, m) + self._calc(i << 1 | 1, m + 1, r, m + 1, t)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    sgt = SegmentTree(nums)
    print(sgt.query(2, 4))
    sgt.update(4, -10)
    print(sgt.query(2, 4))
