# -*- coding: utf-8 -*-
# @Time    : 2021/9/9 10:18
# @File    : 68. 文本左右对齐.py
from leetcode import *


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        tmpStr, strLen = deque(), 0
        ans = []
        for word in words:
            n = len(word)
            if strLen + n + 1 <= maxWidth:
                tmpStr.append(word)
                strLen += n + 1
            elif strLen + n == maxWidth:
                tmp = ''
                while tmpStr:
                    tmp += tmpStr.popleft() + ' '
                strLen = 0
                ans.append(tmp + word)
            else:
                totalSpace = len(tmpStr) + maxWidth - strLen
                if len(tmpStr) == 1:
                    tmp = tmpStr.popleft() + ' ' * (maxWidth - strLen + 1)
                    ans.append(tmp)
                    tmpStr.append(word)
                    strLen = n + 1
                    continue
                eachSpace = totalSpace // (len(tmpStr) - 1)
                tmp = ''
                # startSpace = totalSpace - (eachSpace * (len(tmpStr) - 2))
                # remainSpace = totalSpace - (eachSpace * (len(tmpStr) - 1))
                remainSpace = totalSpace % (len(tmpStr) - 1)
                while tmpStr:
                    if remainSpace > 0:
                        tmp += tmpStr.popleft() + (1 + eachSpace) * ' '
                        remainSpace -= 1
                    else:
                        tmp += tmpStr.popleft() + eachSpace * ' '

                tmpStr.append(word)
                strLen = n + 1
                ans.append(tmp[:-eachSpace])

        if tmpStr:
            tmp = ''
            while tmpStr:
                tmp += tmpStr.popleft() + ' '
            tmp = tmp + ' ' * (maxWidth - len(tmp)) if len(tmp) <= maxWidth else tmp[:-1]
            ans.append(tmp)
        return ans


if __name__ == '__main__':
    words = ["ask", "not", "what", "your", "country", "can", "do", "for", "you", "ask", "what", "you", "can", "do",
             "for", "your", "country"]
    maxWidth = 16
    words = ["What", "must", "be", "shall", "be."]
    maxWidth = 5
    words = ["Here", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 14
    print(Solution().fullJustify(words, maxWidth))
