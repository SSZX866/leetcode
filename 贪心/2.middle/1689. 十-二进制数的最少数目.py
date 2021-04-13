# -*- coding: utf-8 -*-
# @Time    : 2021/3/22 16:47
# @File    : 1689. 十-二进制数的最少数目.py
class Solution:
    def minPartitions(self, n: str) -> int:
        cnt = 0
        while n != '0':
            div = ""
            for zero in [i for i, c in enumerate(n) if c == '0']:
                div += '1' * (zero - len(div))
                div += '0'
            div = div + '1' * (len(n) - len(div))
            # print(n, cnt, div)
            cnt += int(n) // int(div)
            n = str(int(n) % int(div))
        if n != 0: cnt += 1
        return cnt


if __name__ == '__main__':
    n = "32"
    print(Solution().minPartitions(n))