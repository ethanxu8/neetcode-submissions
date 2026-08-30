class Solution:
    def longestPalindrome(self, s: str) -> str:

        def find_palindrome(left, right): 
            while left >= 0 and right < len(s) and s[left] == s[right]: 
                left -= 1
                right += 1
            return left + 1, right - 1
        
        best_left = 0 
        best_right = 0 

        for i in range(len(s)): 

            left, right = find_palindrome(i, i)

            if right - left > best_right - best_left: 
                best_left, best_right = left, right


            left, right = find_palindrome(i, i+1)

            if right - left > best_right - best_left: 
                best_left, best_right = left, right
        
        return s[best_left:best_right+1]
       

# palindrome conditon   
# you have a left and right pointer 

# case 1: palindrome is odd 
    # aba 
    # left == right 
    # left -= 1, right += 1 --> expand outwards
    # return left += 1, right -= 1
        