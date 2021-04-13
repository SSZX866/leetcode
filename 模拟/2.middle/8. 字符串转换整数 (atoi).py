# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 16:23
# @File    : 8. 字符串转换整数 (atoi).py
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s or (s[0] != '+' and s[0] != '-' and not s[0].isdigit()): return 0
        index = 0 if s[0].isdigit() else 1
        while index < len(s) and s[index] == '0': index += 1
        if index < len(s) and not s[index].isdigit() or index == len(s): return 0
        ans = s[0] if not s[0].isdigit() else ''
        for i, c in enumerate(s[index:]):
            if i > 10 + index or not c.isdigit():
                break
            ans += c
        if ans == '-' or ans == '+': return 0
        ans = int(ans)
        ans = ans if ans < 2147483647 else 2147483647
        ans = ans if ans > -2147483648 else -2147483648
        return ans


if __name__ == '__main__':
    s = "4193 with words"
    s = "words and 987"
    s = "-91283472332"
    s = "   -42"
    s = "  0000000000012345678"
    s = "20000000000000000000"
    s = "00000-42a1234"
    s = "    0000000000000   "
    print(Solution().myAtoi(s))
