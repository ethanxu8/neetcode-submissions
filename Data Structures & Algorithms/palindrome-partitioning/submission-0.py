class Solution:
    def partition(self, s: str) -> List[List[str]]:

        result = []
        path = []


        def isPalindrome(substr):
            return substr == substr[::-1]

        def backtrack(start):
            
            # base case 
            if start == len(s): 
                result.append(path[:])
                return 
            

            for end in range(start, len(s)): 

                substr = s[start:end+1]

                if isPalindrome(substr): 
                    path.append(substr)
                    backtrack(end+1)
                    path.pop()   

        backtrack(0) 
        return result
 
        






        # start 


        # 

# base case 

    # if palindrome 
        # result.append(s)
        # eliminate that substring from s
    

    # start --> end 


# return results


