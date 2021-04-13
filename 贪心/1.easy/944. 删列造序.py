from typing import List

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        length = len(A[0])
        A_len = len(A)
        cnt = 0
        for i in range(length):
            for j in range(1, A_len):
                if  A[j][i] < A[j-1][i]:
                    cnt += 1
                    break
        print(list(zip(*A)))
        return cnt

if __name__ == '__main__':
    print(Solution().minDeletionSize(["rrjk","furt","guzm"]))

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        res = 0
        for i in zip(*A):
            if list(i) != sorted(i):
                res += 1
        return res