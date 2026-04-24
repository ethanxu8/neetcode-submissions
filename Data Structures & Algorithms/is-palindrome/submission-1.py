class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        i = 0 
        j = len(s) - 1

        while i < j: 
            while i < j and not s[i].isalnum(): 
                i += 1
            while i < j and not s[j].isalnum(): 
                j -= 1
            if s[i].lower() != s[j].lower(): 
                return False 
            i += 1
            j -= 1
        
        return True




        # join string with spaces and lower all characters 
        # have two pointers one from the beginning one from end
        # and then compare and update each pointer 
        