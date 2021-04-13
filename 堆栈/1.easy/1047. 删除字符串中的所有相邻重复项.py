class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = ['']
        for c in S:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)

if __name__ == '__main__':
    print(Solution().removeDuplicates("abbaca"))