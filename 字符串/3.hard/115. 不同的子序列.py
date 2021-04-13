class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if t == '': return 1
        if s == '':return 0
        cnt = 0
        for i in range(len(s)):
            # print(s,t,i)
            if t[0] == s[i]:
                cnt += self.numDistinct(s[i+1:],t[1:])
        return cnt

if __name__ == '__main__':
    s="adbdadeecadeadeccaeaabdabdbcdabddddabcaaadbabaaedeeddeaeebcdeabcaaaeeaeeabcddcebddebeebedaecccbdcbcedbdaeaedcdebeecdaaedaacadbdccabddaddacdddc"
    t="bcddceeeebecbc"
    print(Solution().numDistinct(s,t))