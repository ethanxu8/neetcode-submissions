class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # sliding window 

        # find the maximum differnece in the array 

        # Base cases
            # if the array is strictly descending, return 0 

        # 10 - 1, 10 - 5, 10 - 6

        maxP = 0 
        minBuy = prices[0]

        for sell in prices: 
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP

 