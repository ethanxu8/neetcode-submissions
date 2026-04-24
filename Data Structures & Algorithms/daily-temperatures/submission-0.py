class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures): 
            if not stack: 
                stack.append((temp, i))
            
            while stack and temp > stack[-1][0]:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()

            stack.append((temp, i))
        
        return res
                


       

       

        # goal: return the number of days after the ith day before a warmer temp 
            # temp a 
            # if b > a, append ind(b) - ind(a) to res 
        
        # Approach: 
            
        # brute force, nested for loop --> O(n^2) time complexity 
        
        # have a stack and add temp a 
        # if temp b higher then append ind(b) - ind(a), else add temp b 
        # if temp c higher than b append ind(c) - ind(b), then check c with a

    # loop through each temp and before adding it into the stack check with existing temp
    # if empty add to stack 
    # if temp > prev temp append diff of indexes and pop that temp out
        