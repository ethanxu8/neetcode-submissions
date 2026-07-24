class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)

        dp = [0] * (n+1)

        dp[0] = 0
        dp[1] = 0

        for i in range(2, n+1): 

            dp[i] = min(
                dp[i-1] + cost[i-1], 
                dp[i-2] + cost[i-2]
            )
        
        return dp[n]



        



# approach 

# n --> len(cost)

# if index > n: then we return tot_cost which we want to minimze 

# dp = [0] * n + 2 --> because we can take two steps 
    # if each dp tracks the min cost up to that point once index > n 
        # return dp[index]
        # dp[i] = cost[i] + cur_cost


# tot_cost = min(tot_cost, cur_cost)




# objective: return min cost to reach the top of staircase 
    # past the last index in cost 
    
    # rules 
        # after paying cost[i], we can go to either cost[i+1] or cost[i+2]


# Example 1: 
    # cost = [1,2,3]
    # start at index 1 so cost[1] == 2 --> pay 2 
    # we take two steps to get past last index and pay 2 

# if index >= len(cost), return tot_cost --> has to be >= since you can skip last index


# Example 2: 
    # cost = [1,2,1,2,1,1,1]
    # cost[0] == 1 --> take two steps 
    # cost[2] == 1 --> take two steps 
    # cost[4] == 1 --> take two stpes 
    # cost[6] == 1 and take one step to reach the top 

# dynamic programming problem 

# there are two courses of action 
    # either take one step --> (i+1) or 
    # take two steps --> (i+2)
        