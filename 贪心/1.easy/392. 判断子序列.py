from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        s_len = len(s)
        t_len = len(t)
        if s_len == 0:
            return True
        while i < t_len:
            if s[j] == t[i]:
                j += 1
                if j == s_len:
                    return True
            i += 1
        return False


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while j < len(t) and i < len(s):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


if __name__ == '__main__':
    print(Solution().isSubsequence(s="axc", t="ahbgdc"))
