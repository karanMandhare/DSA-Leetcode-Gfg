class Solution(object):
    def maxProfit(self, prices):
        max_profit=0
        mini_profit=float("inf")
        n=len(prices)
        for i in range(0,n):
            mini_profit=min(mini_profit,prices[i])
            max_profit=max(max_profit,prices[i]-mini_profit)

        return max_profit
            
       
        