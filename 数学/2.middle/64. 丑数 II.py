# -*- coding: utf-8 -*-
# @Time    : 2021/4/11 12:26
# @File    : 64. 丑数 II.py
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res, i, j = [1], 0, 0
        while i < n:
            nums = [res[i] * 2, res[i] * 3, res[i] * 5]
            for num in nums:
                if num not in res:
                    while res[j] > num:
                        j -= 1
                    res.insert(j + 1, num)
                    j = len(res) - 1
            i += 1
        print(res)
        return res[n - 1]


if __name__ == '__main__':
    print(Solution().nthUglyNumber(27))
