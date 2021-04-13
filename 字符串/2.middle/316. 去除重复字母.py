# -*- coding: utf-8 -*-
# @Time    : 2021/4/7 19:29
# @File    : 316. 去除重复字母.py
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        dic = {}
        s_ = list(set(s))
        seen = set()  # 使用集合空间换时间使时间复杂度由o(n^2)降到o(n)
        for c in s_:
            dic[c] = s.count(c)
        for c in s:
            # if c not in stack:
            if c not in seen:
                while stack and stack[-1] > c and dic[stack[-1]] > 0:
                    # stack.pop()
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
            dic[c] -= 1
            print(stack, dic)
        return "".join(stack)


if __name__ == '__main__':
    s = "abacb"
    print(Solution().removeDuplicateLetters(s))
