from typing import List

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        for i, each in enumerate(A):
            if K < 1:
                break
            if each < 0:
                A[i] = -each
                K -= 1
            if each > 0:
                if K % 2 == 0:
                    break
                else:
                    if A[i] > A[i-1]:
                        A[i-1] = -A[i-1]
                    else:
                        A[i] = -A[i]
                    break
        # result = 0
        # for each in A:
        #     result += each
        # return result
        return sum(A)
    sorted()

if __name__ == '__main__':
    A = [2,-3,-1,5,-4]
    K = 2
    print(Solution().largestSumAfterKNegations(A,K))



