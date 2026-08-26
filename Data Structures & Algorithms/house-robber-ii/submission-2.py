class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1: 
            return nums[0]

        def normal_rob(nums): 
            n = len(nums)
            dp = [0] * (n+1)

            dp[0] = 0 
            dp[1] = nums[0] 

            for i in range(2, n+1): 
                dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
            return dp[n]
        
        max1 = normal_rob(nums[1:])
        max2 = normal_rob(nums[:-1])

        return max(max1, max2)







        # # rob first house, cannot rob last house
        # for i in range(2, n): 
        #     dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        # max1 = dp[n-1]

        # # dp[i-1] --> this can go to n 
        # # dp[i-2] + nums[i-1] --> this can go to n+1
        
        # # cannot rob first house
        # for i in range(4, n+1): 
        #     dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        # max2 = dp[n]

        # return max(max1, max2)



       



# split this into two parts 

# case 1: rob first house but you cannot rob n-1 
# case 2: do not forb first and you can rob n-1

# max(case1, case2) --> only condition: i + i-2 or i-1




    
# goal: return the max amoutn of moeny you can rob w/o alerting police 
    # rule: you cannot rob adjacent houses 

# Examples: 

# nums = [3,4,3]
# adjacent: i and i+1 are adjacent 
# adjacent: 0 and n where n = len(nums)-1 are also adjacent 

# nums = [2,9,8,3,6]
# 9 + 6 = 15 
    # cannot just do i and i + 2 
    
# APPROACH

# EDGE CASE: 
    # If n < 3 --> return max in nums

    # have a list of lenth n, initlaizing all 0s 
    # at each i, have the maximum amount of moeny you can steal 
    # with each new number add that number and the maximum number prev 
        # with following conditions: 
            # curr index cannto add prev index 
            # if curr index is last element in list cant add beginning index 
    
# for loop wouldnt allow us to express the two conditions to chekc adjacnecy 
# exploring every single combination is also time consuming 
    # if we are at i == 100, thats too many potential combos 
    # so we should just have a max until that point that doesnt include the prev i 
        