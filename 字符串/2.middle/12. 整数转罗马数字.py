# -*- coding: utf-8 -*-
# @Time    : 2021/4/15 12:23
# @File    : 12. 整数转罗马数字.py
class Solution:
    def intToRoman(self, num: int) -> str:
        dic = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        num, i, ans = str(num)[::-1], 0, ""
        while i < len(num):
            if '0' < num[i] < '4':
                ans = dic[pow(10, i)] * int(num[i]) + ans
            elif num[i] == '4':
                ans = dic[pow(10, i)] + dic[5 * pow(10, i)] + ans
            elif '4' < num[i] < '9':
                ans = dic[pow(10, i) * 5] + (int(num[i]) - 5) * dic[pow(10, i)] + ans
            elif num[i] == '9':
                ans = dic[pow(10, i)] + dic[pow(10, i + 1)] + ans
            print(ans, i)
            i += 1
        return ans


if __name__ == '__main__':
    print(Solution().intToRoman(230))
