class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == '':
            s = 'a'
        last = False #上一个字符是否为*
        pp = ''
        for c in p:
            if (c == '*' and not last) or c != '*':
                print(c,1111111)
                last = True
                pp += c
                if c != '*':
                    last = False
        print(pp)
        p = pp

        s_len = len(s)
        p_len = len(p)
        i, j = 0, 0 #s,p
        while i < s_len and j < p_len:
            print(i,j)
            if s[i] == p[j] or p[j] == '?':
                i += 1
                j += 1
            elif p[j] == '*':
                if j+1 == p_len:
                    return True
                while i < s_len:

                    print(i, j,1111)
                    if s[i] == p[j+1] or p[j+1] == '?':
                        break
                    i += 1
                j += 1
            else:
                return False
            print(i, j)
        if i == s_len and j == p_len:
            return True
        else:
            return False

if __name__ == '__main__':
    s = ""
    p = "****"
    print(Solution().isMatch(s,p))