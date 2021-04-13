from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cnt = len(prices)
        i = 0
        mark = 0 #状态机 0：初始 1：跌 -1：涨
        bal = 0
        while i < cnt-1:
            if prices[i] != prices[i+1]:
                if mark == 0:
                    if prices[i] > prices[i+1]: #跌
                        mark = 0
                    elif prices[i] < prices[i+1]: #涨
                        mark = -1
                        bal -= prices[i]

                elif mark == -1:
                    if prices[i] > prices[i+1]:
                        bal += prices[i]
                        mark = 1
                        #卖

                elif mark == 1:
                    if prices[i] < prices[i+1]:
                        bal -= prices[i]
                        mark = -1
                        #买
            i += 1
        if mark == -1:
            bal += prices[i]
        return bal

if __name__ == '__main__':
    solotion = Solution()
    print(solotion.maxProfit([1,2,3,4,5]))