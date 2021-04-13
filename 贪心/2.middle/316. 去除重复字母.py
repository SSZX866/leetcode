class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic = list(set(s))
        dic.sort(reverse=True)
        print(dic)

        for c in dic:
            result = ''
            cnt = s.count(c)
            print(cnt)
            if cnt > 1:
                #对于每个重复的字母，从头到尾删除
                for i, C in enumerate(s):
                    if c != C:
                        result += C
                    else:
                        cnt -= 1
                    if cnt == 1:
                        result += s[i+1:]
                        s = result
                        break
                print(result)

        return result

if __name__ == '__main__':
    s = "bcabc"
    s = "cbacdcbc"
    print(Solution().removeDuplicateLetters(s))
    