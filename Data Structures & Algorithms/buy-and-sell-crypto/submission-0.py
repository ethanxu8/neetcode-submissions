class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # sliding window 

        # find the maximum differnece in the array 

        # Base cases
            # if the array is strictly descending, return 0 

        # 10 - 1, 10 - 5, 10 - 6

        l, r = 0, 1
        maxP = 0 

        while r < len(prices): 
            if prices[l] < prices[r]: 
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else: 
                l = r
            r += 1
        return maxP

 