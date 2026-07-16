class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2: 
            return n 

        dp = [0] * (n+1)

        dp[1] = 1
        
        dp[2] = 2
        
        for i in range(3, n + 1): 
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


# base case: 
    # 1 --> 1 way 
    # 2 --> 2 ways 
    # 3 --> 3 ways 
    # 4 --> sum of the previous 
        # 1 + 1 + 1 + 1
        # 1 + 1 + 2
        # 2 + 1 + 1
        # 1 + 2 + 1
        # 2 + 2 
    # dp[3] + dp[1]
        
    # dp[3] = dp[2] + dp[1]