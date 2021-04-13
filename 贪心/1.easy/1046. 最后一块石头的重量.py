from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        while len(stones) > 1:
            print(stones)
            stone = stones[0] - stones[1]
            stones.pop(0)
            stones.pop(0)
            if stone != 0:
                stones.append(stone)
                stones.sort(reverse=True)
        if len(stones) == 1:
            return stones[0]
        else:
            return 0


# class Solution:
#     def lastStoneWeight(self, stones: List[int]) -> int:
#         while len(stones) > 1:
#             i = 0
#             new_stones = []
#             stones.sort()
#             print(stones)
#             while i+1 < len(stones):
#                 if stones[i+1]-stones[i] != 0:
#                     new_stones.append(stones[i+1]-stones[i])
#                 i += 2
#             if i != len(stones):
#                 new_stones.append(stones[i])
#             stones = new_stones
#         if len(stones) == 1:
#             return stones[0]
#         else:
#             return 0
#
if __name__ == '__main__':
    stones = [2,7,4,1,8,1]
    print(Solution().lastStoneWeight(stones))