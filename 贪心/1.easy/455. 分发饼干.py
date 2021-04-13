from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        print(g,s)
        i = 0
        j = 0
        g_len = len(g)
        s_len = len(s)
        while j < s_len:
            if s[j] >= g[i]:
                i += 1
                if i == g_len:
                    return i
            j += 1
        return i

if __name__ == '__main__':
    print(Solution().findContentChildren([10,9,8,7],[5,6,7,8]))