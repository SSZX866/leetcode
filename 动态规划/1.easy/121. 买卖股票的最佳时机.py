from typing import List


#第i天的利润 = Max{第i天价格-前i-1天最小价格， 前i—1天最大利润}

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length == 0:
            return 0
        array = [0 for x in range(length)]
        min = prices[0]

        for i, price in enumerate(prices[1:]):
            #从第二个开始遍历
            array[i] = max(price - min, array[i])
            if price < min:
                min = price
        return max(array)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprcie = float("inf")
        maxprofit = 0
        for price in prices:
            maxprofit = max(maxprofit, price-minprcie)
            minprcie = min(price, minprcie)
        return maxprofit

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(Solution().maxProfit(prices))