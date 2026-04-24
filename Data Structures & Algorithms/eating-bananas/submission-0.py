class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def find_hours(cur_rate, h): 
            cur_hours = 0 
            for pile in piles: 
                cur_hours += -(-pile // rate) 
            return cur_hours


        left, right = 1, max(piles)

        while left <= right: 
            rate = (left + right) // 2

            if find_hours(rate, h) <= h: 
                right = rate - 1
            else: 
                left = rate + 1
        
        return left
              

           
            
           
            


            # check if it can eat within h housrs






        # REACTO 
        # READ, EXAMPLE, APPROACH, CODE, TEST, OPTIMIZE

        # goal: output the minimum eating rate needed to eat all bananas
            # if piles[i] <= rate, you can finish but not move on to another pile 
        
        # Example 1: 
            # minimum to eat all bananas within 9 hours 
            # pile 1 takes 1 hours  --> 1 % 2 --> 0.5 which is 1
            # pile 2 takes 2 hours --> 4 % 2 --> 2 
            # pile 3 takes 2 hours --> 3 % 2 --> 1.5 which is 2
            # pile 4 takes 1 hour --> 2 % 2 --> 1 which is 1 
        

        # Example 2: 
            # pile 1: 25 % 25 --> 1 
            # pile 2: 10 % 25 --> 10/25 so 1 
            # pile 3: 23 % 25 --> 23/25 so 1 
            # pile 4: 4 % 25 --> so 1 

    
        # APPROACH    

        # piles[i] % rate --> upper bound is the number of hours 
        # add those up and they have to be less than h 

        # limitations 
            # len(piles) == 4, hours has to be above 4
            # highest rate possible that can be an answer is max(piles)
            # minimum answer is 1 

            # so from 1 to max(piles) binary search to find an answer 


        








