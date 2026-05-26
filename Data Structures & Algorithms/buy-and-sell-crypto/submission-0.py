class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        maxProfit = 0 
        
        for i in range(0,n-1):
            buyPrice = prices[i]
            for j in range(i+1,n):
                sellPrice = prices[j]
                profit = sellPrice - buyPrice
                maxProfit = max(maxProfit, profit)
        
        return max(maxProfit,0)