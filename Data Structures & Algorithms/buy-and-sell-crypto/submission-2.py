class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        maxProfit = 0 
        l = 0

        for r in range(1,n):
            if prices[l] > prices[r]:
                l=r
            
            else: 
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)

        return maxProfit    
        